import asyncio

import aiosqlite
from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from middlewares.db_middleware import DbMiddleware
from loader import dp, bot
from data.config import ADMINS
from filters import IsPrivate
from keyboards.default import buttons as kb_buttons
from keyboards.default.buttons import admin_button, start_button
from utils.misc import rate_limit
from utils.db import Database

DB_PATH = "main_database.db"
db = Database(DB_PATH)


# =====================================================================
#  DINAMIK MENYU: admin /add orqali tugma + fayl qo'shadi (SQLite'da)
#  Bu handlerlar "import handlers" dan OLDIN ro'yxatdan o'tadi.
# =====================================================================

MAX_NAME_LEN = 64
ROOT_ID = 0
FILE_TYPES = ["document", "photo", "video", "audio", "voice"]

# Asosiy (statik) reply-klaviaturalarning boshlang'ich uzunligi
_STATIC_ROWS = {id(kb): len(kb.keyboard) for kb in (start_button, admin_button)}
# Barcha statik reply tugma matnlari (asosiy menyuda nom to'qnashmasligi uchun)
_STATIC_TEXTS = set()
for _obj in vars(kb_buttons).values():
    if isinstance(_obj, types.ReplyKeyboardMarkup):
        for _row in _obj.keyboard:
            for _btn in _row:
                _text = _btn if isinstance(_btn, str) else _btn.text
                _STATIC_TEXTS.add(_text.strip().lower())

# Asosiy menyudagi dinamik tugmalar: {nom: id}. Har saqlashda yangilanadi.
_root_nodes = {}
# Admin /add jarayonidagi vaqtinchalik ma'lumot: {user_id: {...}}
_pending = {}


class AddMenu(StatesGroup):
    joy_tanlash = State()
    nom_kiritish = State()
    fayl_yuklash = State()


def is_admin(obj) -> bool:
    return bool(obj.from_user) and obj.from_user.id in ADMINS


# ---------------------------- storage ----------------------------

async def menu_create_tables():
    async with aiosqlite.connect(DB_PATH) as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS menu_nodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_id INTEGER NOT NULL DEFAULT 0,
                name TEXT NOT NULL
            )
        """)
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS menu_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                node_id INTEGER NOT NULL,
                file_id TEXT NOT NULL,
                file_type TEXT NOT NULL,
                file_name TEXT
            )
        """)
        await conn.commit()


async def menu_children(parent_id: int):
    async with aiosqlite.connect(DB_PATH) as conn:
        async with conn.execute(
                "SELECT id, name FROM menu_nodes WHERE parent_id = ? ORDER BY id", (parent_id,)) as cur:
            return await cur.fetchall()


async def menu_node(node_id: int):
    """(id, parent_id, name) yoki None"""
    async with aiosqlite.connect(DB_PATH) as conn:
        async with conn.execute(
                "SELECT id, parent_id, name FROM menu_nodes WHERE id = ?", (node_id,)) as cur:
            return await cur.fetchone()


async def menu_files(node_id: int):
    async with aiosqlite.connect(DB_PATH) as conn:
        async with conn.execute(
                "SELECT file_id, file_type, file_name FROM menu_files WHERE node_id = ? ORDER BY id",
                (node_id,)) as cur:
            return await cur.fetchall()


async def menu_add_node(parent_id: int, name: str, files: list) -> int:
    """Tugma va uning fayllarini bitta tranzaksiyada saqlaydi."""
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await conn.execute(
            "INSERT INTO menu_nodes (parent_id, name) VALUES (?, ?)", (parent_id, name))
        node_id = cur.lastrowid
        await conn.executemany(
            "INSERT INTO menu_files (node_id, file_id, file_type, file_name) VALUES (?, ?, ?, ?)",
            [(node_id, f["file_id"], f["type"], f["name"]) for f in files])
        await conn.commit()
        return node_id


async def menu_path(node_id: int) -> str:
    parts = []
    while node_id != ROOT_ID:
        node = await menu_node(node_id)
        if not node:
            break
        parts.append(node[2])
        node_id = node[1]
    return " / ".join(["Asosiy"] + parts[::-1])


async def refresh_main_keyboards():
    """Asosiy menyudagi dinamik tugmalarni bazadan qayta yuklab, reply-klaviaturalarga qo'yadi."""
    await menu_create_tables()
    nodes = await menu_children(ROOT_ID)
    _root_nodes.clear()
    _root_nodes.update({name: node_id for node_id, name in nodes})
    names = [name for _, name in nodes]
    rows = [[types.KeyboardButton(text=n) for n in names[i:i + 2]] for i in range(0, len(names), 2)]
    for kb in (start_button, admin_button):
        kb.keyboard[:] = kb.keyboard[:_STATIC_ROWS[id(kb)]] + rows


# ---------------------------- render ----------------------------

def render_menu(nodes, prefix: str, extra_rows=()) -> types.InlineKeyboardMarkup:
    """Menyu tugmalarini chizadi. Foydalanuvchi menyusi ham, /add ham shu funksiyadan foydalanadi."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*[
        types.InlineKeyboardButton(text=name, callback_data=f"{prefix}:{node_id}")
        for node_id, name in nodes
    ])
    for row in extra_rows:
        markup.row(*row)
    return markup


async def user_menu_markup(node_id: int):
    """Tugma ichidagi tugmalar menyusi (foydalanuvchi uchun)."""
    extra = []
    if node_id != ROOT_ID:
        node = await menu_node(node_id)
        parent_id = node[1] if node else ROOT_ID
        if parent_id != ROOT_ID:
            extra.append([types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"mb:{parent_id}")])
    return render_menu(await menu_children(node_id), "m", extra)


async def send_node_files(chat_id: int, node_id: int) -> int:
    """Tugmaga biriktirilgan fayllarni tartib bilan yuboradi."""
    senders = {
        "document": bot.send_document,
        "photo": bot.send_photo,
        "video": bot.send_video,
        "audio": bot.send_audio,
        "voice": bot.send_voice,
    }
    sent = 0
    for file_id, file_type, _name in await menu_files(node_id):
        try:
            await senders.get(file_type, bot.send_document)(chat_id, file_id)
            sent += 1
        except Exception:
            pass
        await asyncio.sleep(0.05)
    return sent


async def open_node_for_user(chat_id: int, node_id: int, name: str) -> bool:
    """Fayllarni yuboradi, ichki tugmalar bo'lsa menyuni ham ko'rsatadi. Bo'sh bo'lsa False."""
    sent = await send_node_files(chat_id, node_id)
    children = await menu_children(node_id)
    if children:
        await bot.send_message(chat_id, f"📂 {name}\nTanlang! 👇",
                               reply_markup=await user_menu_markup(node_id))
    return bool(sent or children)


# ---------------------------- foydalanuvchi ----------------------------

@dp.message_handler(IsPrivate(), lambda m: bool(m.text) and m.text in _root_nodes)
async def dynamic_root_button(message: types.Message):
    node_id = _root_nodes[message.text]
    if not await open_node_for_user(message.chat.id, node_id, message.text):
        await message.answer("Bu bo'lim hozircha bo'sh.")


@dp.callback_query_handler(lambda c: bool(c.data) and c.data.startswith("m:"))
async def dynamic_inline_button(call: types.CallbackQuery):
    node = await menu_node(int(call.data.split(":")[1]))
    if not node:
        return await call.answer("Bu tugma o'chirilgan.", show_alert=True)
    node_id, _parent, name = node
    files = await menu_files(node_id)
    children = await menu_children(node_id)
    if not files and not children:
        return await call.answer("Bu bo'lim hozircha bo'sh.", show_alert=True)
    await call.answer()
    if files:
        await open_node_for_user(call.message.chat.id, node_id, name)
    else:
        await call.message.edit_text(f"📂 {name}\nTanlang! 👇",
                                     reply_markup=await user_menu_markup(node_id))


@dp.callback_query_handler(lambda c: bool(c.data) and c.data.startswith("mb:"))
async def dynamic_inline_back(call: types.CallbackQuery):
    node = await menu_node(int(call.data.split(":")[1]))
    await call.answer()
    if not node:
        return
    await call.message.edit_text(f"📂 {node[2]}\nTanlang! 👇",
                                 reply_markup=await user_menu_markup(node[0]))


# ---------------------------- admin: /add ----------------------------

def _upload_markup() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(text="💾 Saqlash", callback_data="af:save"),
        types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="af:cancel"),
    )
    return markup


async def _add_tree_view(parent_id: int):
    text = (f"➕ Yangi tugma qo'shish\n\n📍 Joy: {await menu_path(parent_id)}\n\n"
            "Ichiga kirish uchun tugmani bosing yoki shu joyni tanlang.")
    extra = [
        [types.InlineKeyboardButton(text="✅ Shu yerga qo'shish", callback_data="ad:ok")],
        [types.InlineKeyboardButton(text="🏠 Asosiy", callback_data="ad:home"),
         types.InlineKeyboardButton(text="⬅️ Orqaga", callback_data="ad:back")],
        [types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="ad:cancel")],
    ]
    return text, render_menu(await menu_children(parent_id), "ad", extra)


async def _finish_add(state: FSMContext, user_id: int):
    _pending.pop(user_id, None)
    try:
        await state.finish()
    except KeyError:
        await state.set_state(None)


@dp.message_handler(IsPrivate(), is_admin, commands="add", state="*")
async def add_start(message: types.Message, state: FSMContext):
    await menu_create_tables()
    _pending[message.from_user.id] = {"parent": ROOT_ID, "name": None, "files": [], "status_msg": None}
    text, markup = await _add_tree_view(ROOT_ID)
    await message.answer(text, reply_markup=markup)
    await AddMenu.joy_tanlash.set()


@dp.callback_query_handler(is_admin, lambda c: bool(c.data) and c.data.startswith("ad:"),
                           state=AddMenu.joy_tanlash)
async def add_choose_place(call: types.CallbackQuery, state: FSMContext):
    data = _pending.get(call.from_user.id)
    if data is None:
        await _finish_add(state, call.from_user.id)
        return await call.answer("Jarayon eskirgan. /add ni qayta yuboring.", show_alert=True)

    action = call.data.split(":")[1]
    if action == "cancel":
        await _finish_add(state, call.from_user.id)
        await call.message.edit_text("❌ Bekor qilindi.")
        return await call.answer()

    if action == "ok":
        await call.message.edit_text(
            f"📍 Joy: {await menu_path(data['parent'])}\n\n"
            f"✏️ Yangi tugma nomini yuboring ({MAX_NAME_LEN} belgidan oshmasin).\n"
            "Bekor qilish uchun /cancel")
        await AddMenu.nom_kiritish.set()
        return await call.answer()

    if action == "home":
        target = ROOT_ID
    elif action == "back":
        node = await menu_node(data["parent"])
        target = node[1] if node else ROOT_ID
    else:
        node = await menu_node(int(action))
        if not node:
            return await call.answer("Bu tugma topilmadi.", show_alert=True)
        target = node[0]

    if target == data["parent"]:
        return await call.answer("Siz asosiy menyudasiz." if target == ROOT_ID else None)
    data["parent"] = target
    text, markup = await _add_tree_view(target)
    await call.message.edit_text(text, reply_markup=markup)
    await call.answer()


@dp.message_handler(IsPrivate(), is_admin, commands="cancel",
                    state=[AddMenu.joy_tanlash, AddMenu.nom_kiritish, AddMenu.fayl_yuklash])
async def add_cancel_command(message: types.Message, state: FSMContext):
    await _finish_add(state, message.from_user.id)
    await message.answer("❌ Bekor qilindi.", reply_markup=admin_button)


@dp.message_handler(IsPrivate(), is_admin, state=AddMenu.nom_kiritish, content_types=types.ContentTypes.ANY)
async def add_get_name(message: types.Message, state: FSMContext):
    data = _pending.get(message.from_user.id)
    if data is None:
        await _finish_add(state, message.from_user.id)
        return await message.answer("Jarayon eskirgan. /add ni qayta yuboring.")

    name = " ".join((message.text or "").split())
    if not name:
        return await message.answer("⚠️ Nom bo'sh bo'lmasligi kerak. Tugma nomini matn bilan yuboring.")
    if name.startswith("/"):
        return await message.answer("⚠️ Nom \"/\" belgisi bilan boshlanmasin. Boshqa nom yuboring.")
    if len(name) > MAX_NAME_LEN:
        return await message.answer(
            f"⚠️ Nom {MAX_NAME_LEN} belgidan oshmasin (hozir {len(name)} ta). Qisqaroq nom yuboring.")
    siblings = {n.lower() for _, n in await menu_children(data["parent"])}
    if name.lower() in siblings or (data["parent"] == ROOT_ID and name.lower() in _STATIC_TEXTS):
        return await message.answer("⚠️ Bu joyda shu nomli tugma allaqachon bor. Boshqa nom yuboring.")

    data["name"] = name
    msg = await message.answer(
        f"📍 Joy: {await menu_path(data['parent'])}\n🔘 Tugma: {name}\n\n"
        "📎 Fayllarni yuboring, tugagach 💾 Saqlash bosing.",
        reply_markup=_upload_markup())
    data["status_msg"] = msg.message_id
    await AddMenu.fayl_yuklash.set()


@dp.message_handler(IsPrivate(), is_admin, state=AddMenu.fayl_yuklash, content_types=FILE_TYPES)
@rate_limit(0)
async def add_get_file(message: types.Message, state: FSMContext):
    data = _pending.get(message.from_user.id)
    if data is None:
        await _finish_add(state, message.from_user.id)
        return await message.answer("Jarayon eskirgan. /add ni qayta yuboring.")

    if message.document:
        item = ("document", message.document.file_id, message.document.file_name)
    elif message.photo:
        item = ("photo", message.photo[-1].file_id, "Rasm")
    elif message.video:
        item = ("video", message.video.file_id, getattr(message.video, "file_name", None) or "Video")
    elif message.audio:
        item = ("audio", message.audio.file_id,
                getattr(message.audio, "file_name", None) or message.audio.title or "Audio")
    else:
        item = ("voice", message.voice.file_id, "Ovozli xabar")

    # await'dan oldin qo'shiladi — ketma-ket (albom) yuborilganda tartib saqlanadi
    data["files"].append({"type": item[0], "file_id": item[1], "name": item[2]})
    count = len(data["files"])

    old_msg, data["status_msg"] = data["status_msg"], None
    if old_msg:
        try:
            await bot.edit_message_reply_markup(message.chat.id, old_msg, reply_markup=None)
        except Exception:
            pass
    msg = await message.answer(f"✅ {count} ta fayl qo'shildi.\nYana yuboring yoki 💾 Saqlash bosing.",
                               reply_markup=_upload_markup())
    if data["status_msg"] is None and len(data["files"]) == count:
        data["status_msg"] = msg.message_id
    else:
        # shu orada yangi fayl kelgan — tugmalar faqat eng pastdagi xabarda qolsin
        try:
            await msg.edit_reply_markup(reply_markup=None)
        except Exception:
            pass


@dp.message_handler(IsPrivate(), is_admin, state=AddMenu.fayl_yuklash, content_types=types.ContentTypes.ANY)
async def add_wrong_content(message: types.Message):
    await message.answer("⚠️ Faqat fayl (hujjat, rasm, video, audio) yuboring yoki 💾 Saqlash bosing.",
                         reply_markup=_upload_markup())


@dp.callback_query_handler(is_admin, lambda c: bool(c.data) and c.data.startswith("af:"),
                           state=AddMenu.fayl_yuklash)
async def add_save_or_cancel(call: types.CallbackQuery, state: FSMContext):
    data = _pending.get(call.from_user.id)
    action = call.data.split(":")[1]
    try:
        await call.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    if action == "cancel" or data is None:
        await _finish_add(state, call.from_user.id)
        await call.message.answer("❌ Bekor qilindi." if data is not None
                                  else "Jarayon eskirgan. /add ni qayta yuboring.",
                                  reply_markup=admin_button)
        return await call.answer()

    # Saqlash: nom shu orada band bo'lib qolmaganini tekshiramiz
    siblings = {n.lower() for _, n in await menu_children(data["parent"])}
    if data["name"].lower() in siblings:
        await _finish_add(state, call.from_user.id)
        await call.message.answer("⚠️ Bu joyda shu nomli tugma allaqachon bor. /add ni qayta yuboring.",
                                  reply_markup=admin_button)
        return await call.answer()

    files = list(data["files"])
    await menu_add_node(data["parent"], data["name"], files)
    path = await menu_path(data["parent"])
    await _finish_add(state, call.from_user.id)
    await refresh_main_keyboards()
    await call.message.answer(
        f"💾 Saqlandi!\n\n📍 Joy: {path}\n🔘 Tugma: {data['name']}\n📎 Fayllar: {len(files)} ta\n\n"
        "🏠 Asosiy menyu",
        reply_markup=admin_button)
    await call.answer("Saqlandi ✅")


# =====================================================================
#  Mavjud handlerlar (dinamik menyu handlerlaridan keyin ulanadi)
# =====================================================================
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # ✅ 1) DB tablelarni yaratib olamiz (users, groups)
    await db.create_table()

    # ✅ Dinamik menyu jadvallari va asosiy menyudagi yangi tugmalar
    await refresh_main_keyboards()

    # ✅ 2) Middleware'ni shu yerda ulash ham xavfsizroq
    dispatcher.middleware.setup(DbMiddleware())

    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
