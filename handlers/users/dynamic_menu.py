"""
Dinamik menyu: admin bot ichidan tugma qo'shadi, o'zgartiradi va o'chiradi (SQLite'da saqlanadi).

- Har bir tugma kontent (matn va/yoki fayllar) yuborishi VA ichida boshqa tugmalarni saqlashi mumkin.
- Tugma ikki turda bo'ladi:
    "reply"  — oddiy (asosiy menyudagidek, pastki klaviaturada chiqadigan) tugma;
    "inline" — xabar ostida chiqadigan tugma.
- Asosiy menyudagi tugmalar har doim oddiy bo'ladi.

Bu modul handlers.users ichida BIRINCHI import qilinadi, shunda uning handlerlari
statik menyu handlerlaridan oldin ro'yxatdan o'tadi.
"""
import asyncio
import logging

import aiosqlite
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import MessageNotModified

from loader import dp, bot
from data.config import ADMINS
from filters import IsPrivate
from keyboards.default import buttons as kb_buttons
from keyboards.default.buttons import admin_button, start_button
from utils.misc import rate_limit

DB_PATH = "main_database.db"

MAX_NAME_LEN = 64
ROOT_ID = 0
REPLY, INLINE = "reply", "inline"
KIND_ICON = {REPLY: "⌨️", INLINE: "🔗"}
KIND_TITLE = {REPLY: "⌨️ oddiy (menyu tugmasi)", INLINE: "🔗 inline (xabar ostida)"}

ADMIN_BTN = "⚙️ Tugmalarni boshqarish"
BACK_BTN = "⬅️ Orqaga"
HOME_BTN = "🏠 Asosiy menyu"
RESERVED_TEXTS = {BACK_BTN.lower(), HOME_BTN.lower(), ADMIN_BTN.lower()}

CONTENT_TYPES = ["text", "document", "photo", "video", "audio", "voice", "animation", "video_note", "sticker"]

# Asosiy (statik) reply-klaviaturalarning boshlang'ich uzunligi
_STATIC_ROWS = {id(kb): len(kb.keyboard) for kb in (start_button, admin_button)}
# Barcha statik reply tugma matnlari — oddiy tugma nomi ular bilan to'qnashmasligi kerak
_STATIC_TEXTS = set()
for _obj in vars(kb_buttons).values():
    if isinstance(_obj, types.ReplyKeyboardMarkup):
        for _row in _obj.keyboard:
            for _btn in _row:
                _text = _btn if isinstance(_btn, str) else _btn.text
                _STATIC_TEXTS.add(_text.strip().lower())

# Kesh: butun menyu daraxti xotirada turadi, har o'zgarishda bazadan qayta yuklanadi
_nodes = {}  # {id: {"parent": int, "name": str, "kind": str}}
_kids = {}   # {parent_id: [id, ...]} — qo'shilgan tartibda
_pos = {}    # {user_id: node_id} — foydalanuvchi hozir qaysi oddiy menyu ichida
_pending = {}  # admin jarayonidagi vaqtinchalik ma'lumot: {user_id: {...}}


class MenuAdmin(StatesGroup):
    nom = State()      # yangi tugma nomi
    kontent = State()  # matn/fayllar yuklash
    rename = State()   # mavjud tugma nomini o'zgartirish


def is_admin(obj) -> bool:
    return bool(obj.from_user) and obj.from_user.id in ADMINS


def _main_keyboard(user_id: int):
    return admin_button if user_id in ADMINS else start_button


# ============================== storage ==============================

async def _create_tables():
    async with aiosqlite.connect(DB_PATH) as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS menu_nodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_id INTEGER NOT NULL DEFAULT 0,
                name TEXT NOT NULL,
                kind TEXT
            )
        """)
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS menu_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                node_id INTEGER NOT NULL,
                file_id TEXT NOT NULL,
                file_type TEXT NOT NULL,
                file_name TEXT,
                caption TEXT
            )
        """)
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS menu_pos (
                user_id BIGINT PRIMARY KEY,
                node_id INTEGER NOT NULL
            )
        """)
        # Eski bazalar uchun yangi ustunlar
        for table, column in (("menu_nodes", "kind"), ("menu_files", "caption")):
            async with conn.execute(f"PRAGMA table_info({table})") as cur:
                columns = {row[1] for row in await cur.fetchall()}
            if column not in columns:
                await conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} TEXT")

        # Turi belgilanmagan (eski) tugmalar: oddiy tugmaga aylantiriladi,
        # nomi statik tugma bilan to'qnashsa — inline bo'lib qoladi.
        async with conn.execute("SELECT id, parent_id, name FROM menu_nodes WHERE kind IS NULL") as cur:
            legacy = await cur.fetchall()
        for node_id, parent_id, name in legacy:
            clash = name.strip().lower() in (_STATIC_TEXTS | RESERVED_TEXTS)
            kind = REPLY if parent_id == ROOT_ID or not clash else INLINE
            await conn.execute("UPDATE menu_nodes SET kind = ? WHERE id = ?", (kind, node_id))
        await conn.commit()


async def refresh_menu():
    """Jadvallarni tayyorlaydi, keshni bazadan qayta yuklaydi va asosiy klaviaturalarni yangilaydi."""
    await _create_tables()
    async with aiosqlite.connect(DB_PATH) as conn:
        async with conn.execute("SELECT id, parent_id, name, kind FROM menu_nodes ORDER BY id") as cur:
            rows = await cur.fetchall()
        if not _pos:
            async with conn.execute("SELECT user_id, node_id FROM menu_pos") as cur:
                _pos.update({user_id: node_id for user_id, node_id in await cur.fetchall()})

    _nodes.clear()
    _kids.clear()
    for node_id, parent_id, name, kind in rows:
        _nodes[node_id] = {"parent": parent_id, "name": name, "kind": kind or INLINE}
        _kids.setdefault(parent_id, []).append(node_id)

    names = [_nodes[i]["name"] for i in _kids.get(ROOT_ID, [])]
    rows = [[types.KeyboardButton(text=n) for n in names[i:i + 2]] for i in range(0, len(names), 2)]
    for kb in (start_button, admin_button):
        kb.keyboard[:] = kb.keyboard[:_STATIC_ROWS[id(kb)]] + rows


async def _execute(sql: str, params=(), many: bool = False):
    async with aiosqlite.connect(DB_PATH) as conn:
        cur = await (conn.executemany(sql, params) if many else conn.execute(sql, params))
        await conn.commit()
        return cur.lastrowid


async def node_items(node_id: int):
    """Tugma kontenti: [(turi, file_id, matn/caption), ...] tartib bilan."""
    async with aiosqlite.connect(DB_PATH) as conn:
        async with conn.execute(
                "SELECT file_type, file_id, caption FROM menu_files WHERE node_id = ? ORDER BY id",
                (node_id,)) as cur:
            return await cur.fetchall()


async def add_items(node_id: int, items: list):
    await _execute(
        "INSERT INTO menu_files (node_id, file_id, file_type, file_name, caption) VALUES (?, ?, ?, ?, ?)",
        [(node_id, it["file_id"], it["type"], it["name"], it["caption"]) for it in items], many=True)


async def add_node(parent_id: int, name: str, kind: str, items: list) -> int:
    node_id = await _execute(
        "INSERT INTO menu_nodes (parent_id, name, kind) VALUES (?, ?, ?)", (parent_id, name, kind))
    if items:
        await add_items(node_id, items)
    return node_id


async def delete_subtree(node_id: int) -> int:
    """Tugmani ichidagi barcha tugmalar va kontenti bilan o'chiradi. O'chirilganlar sonini qaytaradi."""
    ids = _subtree_ids(node_id)
    marks = ",".join("?" * len(ids))
    async with aiosqlite.connect(DB_PATH) as conn:
        await conn.execute(f"DELETE FROM menu_files WHERE node_id IN ({marks})", ids)
        await conn.execute(f"DELETE FROM menu_nodes WHERE id IN ({marks})", ids)
        await conn.commit()
    return len(ids)


async def set_pos(user_id: int, node_id: int):
    if _pos.get(user_id, ROOT_ID) == node_id:
        return
    _pos[user_id] = node_id
    try:
        await _execute("INSERT OR REPLACE INTO menu_pos (user_id, node_id) VALUES (?, ?)", (user_id, node_id))
    except Exception:
        logging.exception("menu_pos saqlanmadi")


# ============================== daraxt yordamchilari ==============================

def _children(parent_id: int, kind: str = None) -> list:
    ids = _kids.get(parent_id, [])
    return [i for i in ids if kind is None or _nodes[i]["kind"] == kind]


def _subtree_ids(node_id: int) -> list:
    ids, queue = [], [node_id]
    while queue:
        current = queue.pop()
        ids.append(current)
        queue.extend(_kids.get(current, []))
    return ids


def _parent(node_id: int) -> int:
    node = _nodes.get(node_id)
    return node["parent"] if node else ROOT_ID


def _path(node_id: int) -> str:
    parts = []
    while node_id != ROOT_ID and node_id in _nodes:
        parts.append(_nodes[node_id]["name"])
        node_id = _nodes[node_id]["parent"]
    return " / ".join(["Asosiy"] + parts[::-1])


def _user_pos(user_id: int) -> int:
    pos = _pos.get(user_id, ROOT_ID)
    return pos if pos in _nodes else ROOT_ID


def _validate_name(name: str, parent_id: int, kind: str, skip_id: int = None):
    """Nom yaroqli bo'lsa None, aks holda xato matnini qaytaradi."""
    if not name:
        return "⚠️ Nom bo'sh bo'lmasligi kerak. Tugma nomini matn bilan yuboring."
    if name.startswith("/"):
        return "⚠️ Nom \"/\" belgisi bilan boshlanmasin. Boshqa nom yuboring."
    if len(name) > MAX_NAME_LEN:
        return f"⚠️ Nom {MAX_NAME_LEN} belgidan oshmasin (hozir {len(name)} ta). Qisqaroq nom yuboring."
    low = name.lower()
    if any(_nodes[i]["name"].lower() == low for i in _children(parent_id) if i != skip_id):
        return "⚠️ Bu joyda shu nomli tugma allaqachon bor. Boshqa nom yuboring."
    if kind == REPLY and low in (_STATIC_TEXTS | RESERVED_TEXTS):
        return ("⚠️ Bu nom botning mavjud menyu tugmasi bilan bir xil — oddiy tugma uchun ishlatib bo'lmaydi.\n"
                "Boshqa nom yuboring (yoki tugmani inline turida qo'shing).")
    return None


# ============================== foydalanuvchi tomoni ==============================

def _reply_keyboard(node_id: int) -> types.ReplyKeyboardMarkup:
    """Tugma ichidagi oddiy tugmalar — asosiy menyudagidek pastki klaviatura."""
    names = [_nodes[i]["name"] for i in _children(node_id, REPLY)]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(names), 2):
        markup.row(*[types.KeyboardButton(text=n) for n in names[i:i + 2]])
    markup.row(types.KeyboardButton(text=BACK_BTN), types.KeyboardButton(text=HOME_BTN))
    return markup


def _inline_keyboard(node_id: int, origin: int) -> types.InlineKeyboardMarkup:
    """
    Tugma ichidagi inline tugmalar. origin — shu xabar dastlab qaysi tugmaga tegishli bo'lgani:
    xabar ichida chuqurroq kirilganda "Orqaga" tugmasi chiqadi.
    """
    ids = _children(node_id, INLINE)
    width = 1 if any(len(_nodes[i]["name"]) > 20 for i in ids) else 2
    markup = types.InlineKeyboardMarkup(row_width=width)
    markup.add(*[types.InlineKeyboardButton(text=_nodes[i]["name"], callback_data=f"m:{i}:{origin}")
                 for i in ids])
    if node_id != origin:
        markup.row(types.InlineKeyboardButton(text=BACK_BTN, callback_data=f"mb:{_parent(node_id)}:{origin}"))
    return markup


async def _send_item(chat_id: int, item, markup=None):
    file_type, file_id, caption = item
    if file_type == "text":
        return await bot.send_message(chat_id, caption, parse_mode="HTML", reply_markup=markup)
    if file_type == "sticker":
        return await bot.send_sticker(chat_id, file_id, reply_markup=markup)
    if file_type == "video_note":
        return await bot.send_video_note(chat_id, file_id, reply_markup=markup)
    sender = {
        "photo": bot.send_photo,
        "video": bot.send_video,
        "audio": bot.send_audio,
        "voice": bot.send_voice,
        "animation": bot.send_animation,
    }.get(file_type, bot.send_document)
    return await sender(chat_id, file_id, caption=caption or None,
                        parse_mode="HTML" if caption else None, reply_markup=markup)


async def open_node(chat_id: int, user_id: int, node_id: int) -> bool:
    """
    Tugmani ochadi: avval kontentni (matn/fayllar) yuboradi, izidan ichidagi tugmalarni chiqaradi.
    Tugma butunlay bo'sh bo'lsa False qaytaradi.
    """
    name = _nodes[node_id]["name"]
    items = await node_items(node_id)
    has_reply = bool(_children(node_id, REPLY))
    has_inline = bool(_children(node_id, INLINE))
    if not items and not has_reply and not has_inline:
        return False

    header = f"📂 {name}\nTanlang! 👇"
    reply_kb = _reply_keyboard(node_id) if has_reply else None
    inline_kb = _inline_keyboard(node_id, node_id) if has_inline else None
    if reply_kb and inline_kb:
        # Bitta xabarga ikkala klaviatura sig'maydi: oddiy menyu alohida xabar bilan o'rnatiladi
        await bot.send_message(chat_id, f"📂 {name}", reply_markup=reply_kb)
        header = "Tanlang! 👇"
    markup = inline_kb or reply_kb

    # Tugmalar oxirgi kontent xabariga biriktiriladi: "matn yuboriladi, izidan tugmalar chiqadi"
    delivered = markup is None
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        try:
            await _send_item(chat_id, item, markup if is_last else None)
            delivered = delivered or is_last
        except Exception:
            logging.exception("Menyu kontenti yuborilmadi (node=%s)", node_id)
        await asyncio.sleep(0.05)
    if not delivered:
        await bot.send_message(chat_id, header, reply_markup=markup)

    if has_reply:
        await set_pos(user_id, node_id)
    return True


def _resolve_button(message: types.Message):
    """Bosilgan oddiy tugma matniga mos dinamik tugma id sini topadi (bo'lmasa None)."""
    text = message.text
    if not text or not message.from_user:
        return None
    pos = _user_pos(message.from_user.id)
    for parent_id in dict.fromkeys((pos, ROOT_ID)):
        for node_id in _children(parent_id, REPLY):
            if _nodes[node_id]["name"] == text:
                return node_id
    # Bot qayta ishga tushgan yoki klaviatura eskirgan bo'lsa — nom bo'yicha qidiramiz
    if text.strip().lower() not in _STATIC_TEXTS:
        for node_id, node in _nodes.items():
            if node["kind"] == REPLY and node["name"] == text:
                return node_id
    return None


@dp.message_handler(IsPrivate(), lambda m: _resolve_button(m) is not None)
async def dynamic_reply_button(message: types.Message):
    node_id = _resolve_button(message)
    if node_id is None:
        return
    if not await open_node(message.chat.id, message.from_user.id, node_id):
        await message.answer("Bu bo'lim hozircha bo'sh.")


@dp.message_handler(IsPrivate(), text=[BACK_BTN, HOME_BTN])
async def dynamic_reply_nav(message: types.Message):
    user_id = message.from_user.id
    target = ROOT_ID
    if message.text == BACK_BTN:
        # Oddiy tugmalari bor eng yaqin yuqori bo'limga qaytamiz
        target = _parent(_user_pos(user_id))
        while target != ROOT_ID and not _children(target, REPLY):
            target = _parent(target)
    await set_pos(user_id, target)
    if target == ROOT_ID:
        await message.answer("🏠 Asosiy menyu", reply_markup=_main_keyboard(user_id))
    else:
        await message.answer(f"📂 {_nodes[target]['name']}\nTanlang! 👇", reply_markup=_reply_keyboard(target))


@dp.callback_query_handler(lambda c: bool(c.data) and c.data.startswith("m:"), state="*")
async def dynamic_inline_button(call: types.CallbackQuery):
    parts = call.data.split(":")
    node_id = int(parts[1])
    origin = int(parts[2]) if len(parts) > 2 else None
    if node_id not in _nodes:
        return await call.answer("Bu tugma o'chirilgan.", show_alert=True)

    has_content = bool(await node_items(node_id))
    has_reply = bool(_children(node_id, REPLY))
    has_inline = bool(_children(node_id, INLINE))
    if not has_content and not has_reply and not has_inline:
        return await call.answer("Bu bo'lim hozircha bo'sh.", show_alert=True)

    if origin is not None and not has_content and not has_reply:
        # Faqat inline tugmalari bor bo'lim — shu xabarning o'zida ochiladi
        try:
            await call.message.edit_reply_markup(reply_markup=_inline_keyboard(node_id, origin))
        except MessageNotModified:
            pass
        return await call.answer(f"📂 {_nodes[node_id]['name']}")

    await call.answer()
    await open_node(call.message.chat.id, call.from_user.id, node_id)


@dp.callback_query_handler(lambda c: bool(c.data) and c.data.startswith("mb:"), state="*")
async def dynamic_inline_back(call: types.CallbackQuery):
    parts = call.data.split(":")
    node_id = int(parts[1])
    origin = int(parts[2]) if len(parts) > 2 else node_id
    if node_id not in _nodes:
        return await call.answer("Bu bo'lim o'chirilgan.", show_alert=True)
    try:
        await call.message.edit_reply_markup(reply_markup=_inline_keyboard(node_id, origin))
    except MessageNotModified:
        pass
    await call.answer()


# ============================== admin: boshqaruv paneli ==============================

def _btn(text: str, data: str) -> types.InlineKeyboardButton:
    return types.InlineKeyboardButton(text=text, callback_data=data)


def _upload_markup() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(row_width=2).add(
        _btn("💾 Saqlash", "af:save"), _btn("❌ Bekor qilish", "af:cancel"))


async def _reset(state: FSMContext, user_id: int):
    """Admin jarayonini (nom kiritish / kontent yuklash) to'xtatadi."""
    data = _pending.pop(user_id, None)
    if data and data.get("status_msg"):
        try:
            await bot.edit_message_reply_markup(user_id, data["status_msg"], reply_markup=None)
        except Exception:
            pass
    if await state.get_state() is not None:
        try:
            await state.finish()
        except KeyError:
            await state.set_state(None)


def _content_summary(items) -> str:
    texts = sum(1 for it in items if it[0] == "text")
    files = len(items) - texts
    parts = ([f"{texts} ta matn"] if texts else []) + ([f"{files} ta fayl"] if files else [])
    return ", ".join(parts) or "yo'q"


async def _panel_view(node_id: int):
    kids = _children(node_id)
    lines = ["⚙️ Tugmalarni boshqarish", "", f"📍 Joy: {_path(node_id)}"]
    if node_id != ROOT_ID:
        lines.append(f"🔘 Turi: {KIND_TITLE[_nodes[node_id]['kind']]}")
        lines.append(f"📎 Kontent: {_content_summary(await node_items(node_id))}")
    lines.append(f"📂 Ichidagi tugmalar: {len(kids)} ta")
    if kids:
        lines += ["", "Ichiga kirish uchun tugmani bosing (⌨️ oddiy, 🔗 inline)."]

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(*[_btn(f"{KIND_ICON[_nodes[i]['kind']]} {_nodes[i]['name']}", f"a:go:{i}") for i in kids])
    markup.row(_btn("➕ Shu yerga tugma qo'shish", f"a:add:{node_id}"))
    if node_id != ROOT_ID:
        markup.row(_btn("✏️ Nomini o'zgartirish", f"a:ren:{node_id}"), _btn("📝 Kontent", f"a:cnt:{node_id}"))
        markup.row(_btn("🔁 Turini o'zgartirish", f"a:kind:{node_id}"), _btn("🗑 O'chirish", f"a:del:{node_id}"))
        markup.row(_btn(BACK_BTN, f"a:go:{_parent(node_id)}"), _btn("🏠 Asosiy", f"a:go:{ROOT_ID}"))
    markup.row(_btn("❌ Yopish", "a:close"))
    return "\n".join(lines), markup


async def _content_view(node_id: int):
    items = await node_items(node_id)
    text = (f"📝 Kontent\n\n📍 Tugma: {_path(node_id)}\n📎 Hozir: {_content_summary(items)}\n\n"
            "Kontent — tugma bosilganda yuboriladigan matn va fayllar. "
            "Ichidagi tugmalar kontentdan keyin chiqadi.")
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(_btn("➕ Ustiga qo'shish", f"a:cnta:{node_id}"),
               _btn("♻️ Yangisiga almashtirish", f"a:cntr:{node_id}"))
    if items:
        markup.add(_btn("👁 Ko'rish", f"a:cntv:{node_id}"), _btn("🧹 Tozalash", f"a:cntc:{node_id}"))
    markup.add(_btn(BACK_BTN, f"a:go:{node_id}"))
    return text, markup


async def _show(call: types.CallbackQuery, text: str, markup=None):
    try:
        await call.message.edit_text(text, reply_markup=markup)
    except MessageNotModified:
        pass
    except Exception:
        await call.message.answer(text, reply_markup=markup)


@dp.message_handler(IsPrivate(), is_admin, commands=["menu", "add", "tugmalar"], state="*")
@dp.message_handler(IsPrivate(), is_admin, text=ADMIN_BTN, state="*")
async def panel_open(message: types.Message, state: FSMContext):
    await _reset(state, message.from_user.id)
    await refresh_menu()
    text, markup = await _panel_view(ROOT_ID)
    await message.answer(text, reply_markup=markup)


@dp.message_handler(IsPrivate(), is_admin, commands="cancel",
                    state=[MenuAdmin.nom, MenuAdmin.kontent, MenuAdmin.rename])
async def panel_cancel_command(message: types.Message, state: FSMContext):
    await _reset(state, message.from_user.id)
    await message.answer("❌ Bekor qilindi.", reply_markup=admin_button)


async def _ask_name(call: types.CallbackQuery, parent_id: int, kind: str):
    _pending[call.from_user.id] = {"mode": "add", "parent": parent_id, "kind": kind, "name": None,
                                   "items": [], "status_msg": None}
    await MenuAdmin.nom.set()
    await _show(call,
                f"➕ Yangi tugma\n\n📍 Joy: {_path(parent_id)}\n🔘 Turi: {KIND_TITLE[kind]}\n\n"
                f"✏️ Tugma nomini yuboring ({MAX_NAME_LEN} belgidan oshmasin).",
                types.InlineKeyboardMarkup().add(_btn("❌ Bekor qilish", f"a:go:{parent_id}")))


async def _ask_content(chat_id: int, user_id: int, intro: str):
    msg = await bot.send_message(
        chat_id,
        f"{intro}\n\n"
        "📎 Endi kontent yuboring: matn, hujjat, rasm, video, audio — bir nechta bo'lishi mumkin, "
        "yuborilgan tartibda saqlanadi.\n"
        "Kontent kerak bo'lmasa (faqat ichida tugmalar bo'ladigan bo'lim) — darhol 💾 Saqlash bosing.",
        reply_markup=_upload_markup())
    _pending[user_id]["status_msg"] = msg.message_id
    await MenuAdmin.kontent.set()


@dp.callback_query_handler(is_admin, lambda c: bool(c.data) and c.data.startswith("a:"), state="*")
async def panel_callback(call: types.CallbackQuery, state: FSMContext):
    parts = call.data.split(":")
    action = parts[1]
    node_id = int(parts[2]) if len(parts) > 2 else ROOT_ID
    user_id = call.from_user.id
    await _reset(state, user_id)  # paneldagi har qanday tugma boshlangan jarayonni bekor qiladi

    if action == "close":
        try:
            await call.message.delete()
        except Exception:
            await _show(call, "Panel yopildi.")
        return await call.answer()

    if node_id != ROOT_ID and node_id not in _nodes:
        await call.answer("Bu tugma topilmadi (o'chirilgan bo'lishi mumkin).", show_alert=True)
        return await _show(call, *await _panel_view(ROOT_ID))

    if action == "go":
        await _show(call, *await _panel_view(node_id))

    elif action == "add":
        if node_id == ROOT_ID:
            # Asosiy menyu — pastki klaviatura, u yerda faqat oddiy tugma bo'ladi
            await _ask_name(call, ROOT_ID, REPLY)
        else:
            replies, inlines = len(_children(node_id, REPLY)), len(_children(node_id, INLINE))
            now = f"{replies} ta oddiy, {inlines} ta inline tugma" if replies or inlines else "tugma yo'q"
            markup = types.InlineKeyboardMarkup(row_width=1).add(
                _btn("⌨️ Oddiy tugma (asosiy menyudagidek)", f"a:addk:{node_id}:r"),
                _btn("🔗 Inline tugma (xabar ostida)", f"a:addk:{node_id}:i"),
                _btn(BACK_BTN, f"a:go:{node_id}"))
            await _show(call,
                        f"➕ Yangi tugma\n\n📍 Joy: {_path(node_id)}\n📂 Bu joyda hozir: {now}\n\n"
                        "Qaysi turdagi tugma qo'shasiz?\n\n"
                        "⌨️ Oddiy — bosilganda pastki klaviatura shu bo'lim tugmalariga almashadi.\n"
                        "🔗 Inline — tugmalar xabarning ostida chiqadi.",
                        markup)

    elif action == "addk":
        await _ask_name(call, node_id, INLINE if parts[3:] == ["i"] else REPLY)

    elif action == "ren":
        _pending[user_id] = {"mode": "rename", "node": node_id}
        await MenuAdmin.rename.set()
        await _show(call,
                    f"✏️ Nomini o'zgartirish\n\n📍 Tugma: {_path(node_id)}\n\n"
                    f"Yangi nomni yuboring ({MAX_NAME_LEN} belgidan oshmasin).",
                    types.InlineKeyboardMarkup().add(_btn("❌ Bekor qilish", f"a:go:{node_id}")))

    elif action == "cnt":
        await _show(call, *await _content_view(node_id))

    elif action in ("cnta", "cntr"):
        mode = "append" if action == "cnta" else "replace"
        _pending[user_id] = {"mode": mode, "node": node_id, "items": [], "status_msg": None}
        try:
            await call.message.edit_reply_markup(reply_markup=None)
        except Exception:
            pass
        title = "➕ Kontent ustiga qo'shish" if mode == "append" else "♻️ Kontentni almashtirish"
        await _ask_content(call.message.chat.id, user_id, f"{title}\n📍 Tugma: {_path(node_id)}")

    elif action == "cntv":
        await call.answer()
        for item in await node_items(node_id):
            try:
                await _send_item(call.message.chat.id, item)
            except Exception:
                await call.message.answer("⚠️ Bu element yuborilmadi (fayl buzilgan bo'lishi mumkin).")
            await asyncio.sleep(0.05)
        try:
            await call.message.delete()
        except Exception:
            pass
        text, markup = await _content_view(node_id)
        return await call.message.answer(text, reply_markup=markup)

    elif action == "cntc":
        await _execute("DELETE FROM menu_files WHERE node_id = ?", (node_id,))
        await call.answer("Kontent tozalandi ✅")
        return await _show(call, *await _content_view(node_id))

    elif action == "kind":
        node = _nodes[node_id]
        if node["parent"] == ROOT_ID:
            return await call.answer(
                "Asosiy menyudagi tugmalar faqat oddiy bo'ladi — turini o'zgartirib bo'lmaydi.",
                show_alert=True)
        new_kind = INLINE if node["kind"] == REPLY else REPLY
        if new_kind == REPLY and node["name"].lower() in (_STATIC_TEXTS | RESERVED_TEXTS):
            return await call.answer(
                "Bu nom botning mavjud menyu tugmasi bilan bir xil. Avval nomini o'zgartiring.",
                show_alert=True)
        await _execute("UPDATE menu_nodes SET kind = ? WHERE id = ?", (new_kind, node_id))
        await refresh_menu()
        await call.answer(f"Endi: {KIND_TITLE[new_kind]}")
        return await _show(call, *await _panel_view(node_id))

    elif action == "del":
        inner = len(_subtree_ids(node_id)) - 1
        extra = f" va ichidagi {inner} ta tugma" if inner else ""
        markup = types.InlineKeyboardMarkup(row_width=2).add(
            _btn("✅ Ha, o'chirish", f"a:delok:{node_id}"), _btn("⬅️ Yo'q", f"a:go:{node_id}"))
        await _show(call,
                    f"🗑 O'chirish\n\n📍 Tugma: {_path(node_id)}\n\n"
                    f"«{_nodes[node_id]['name']}»{extra} butun kontenti bilan o'chiriladi. "
                    "Buni qaytarib bo'lmaydi. Ishonchingiz komilmi?",
                    markup)

    elif action == "delok":
        parent_id = _parent(node_id)
        count = await delete_subtree(node_id)
        await refresh_menu()
        await call.answer(f"O'chirildi: {count} ta tugma ✅")
        return await _show(call, *await _panel_view(parent_id))

    await call.answer()


@dp.message_handler(IsPrivate(), is_admin, state=MenuAdmin.nom, content_types=types.ContentTypes.ANY)
async def panel_get_name(message: types.Message, state: FSMContext):
    data = _pending.get(message.from_user.id)
    if data is None or data.get("mode") != "add":
        await _reset(state, message.from_user.id)
        return await message.answer("Jarayon eskirgan. /menu ni qayta yuboring.")

    name = " ".join((message.text or "").split())
    error = _validate_name(name, data["parent"], data["kind"])
    if error:
        return await message.answer(error)

    data["name"] = name
    await _ask_content(message.chat.id, message.from_user.id,
                       f"📍 Joy: {_path(data['parent'])}\n🔘 Tugma: {name} ({KIND_TITLE[data['kind']]})")


@dp.message_handler(IsPrivate(), is_admin, state=MenuAdmin.rename, content_types=types.ContentTypes.ANY)
async def panel_rename(message: types.Message, state: FSMContext):
    data = _pending.get(message.from_user.id)
    node = _nodes.get(data["node"]) if data and data.get("mode") == "rename" else None
    if node is None:
        await _reset(state, message.from_user.id)
        return await message.answer("Jarayon eskirgan. /menu ni qayta yuboring.")

    name = " ".join((message.text or "").split())
    error = _validate_name(name, node["parent"], node["kind"], skip_id=data["node"])
    if error:
        return await message.answer(error)

    await _execute("UPDATE menu_nodes SET name = ? WHERE id = ?", (name, data["node"]))
    await _reset(state, message.from_user.id)
    await refresh_menu()
    await message.answer(f"✅ Nom o'zgartirildi: {name}", reply_markup=admin_button)
    text, markup = await _panel_view(data["node"])
    await message.answer(text, reply_markup=markup)


def _extract_item(message: types.Message):
    """Xabardan saqlanadigan kontent elementini ajratadi (mos kelmasa None)."""
    caption = message.html_text if (message.text or message.caption) else None
    if message.text:
        return {"type": "text", "file_id": "", "name": None, "caption": caption}
    if message.animation:  # GIF'da document ham bo'ladi — shuning uchun avval tekshiriladi
        return {"type": "animation", "file_id": message.animation.file_id, "name": "GIF", "caption": caption}
    if message.document:
        return {"type": "document", "file_id": message.document.file_id,
                "name": message.document.file_name, "caption": caption}
    if message.photo:
        return {"type": "photo", "file_id": message.photo[-1].file_id, "name": "Rasm", "caption": caption}
    if message.video:
        return {"type": "video", "file_id": message.video.file_id, "name": "Video", "caption": caption}
    if message.audio:
        return {"type": "audio", "file_id": message.audio.file_id,
                "name": message.audio.title or "Audio", "caption": caption}
    if message.voice:
        return {"type": "voice", "file_id": message.voice.file_id, "name": "Ovozli xabar", "caption": caption}
    if message.video_note:
        return {"type": "video_note", "file_id": message.video_note.file_id, "name": "Video xabar",
                "caption": None}
    if message.sticker:
        return {"type": "sticker", "file_id": message.sticker.file_id, "name": "Stiker", "caption": None}
    return None


@dp.message_handler(IsPrivate(), is_admin, state=MenuAdmin.kontent, content_types=types.ContentTypes.ANY)
@rate_limit(0)
async def panel_get_content(message: types.Message, state: FSMContext):
    data = _pending.get(message.from_user.id)
    if data is None or "items" not in data:
        await _reset(state, message.from_user.id)
        return await message.answer("Jarayon eskirgan. /menu ni qayta yuboring.")

    item = None if (message.text or "").startswith("/") else _extract_item(message)
    if item is None:
        return await message.answer(
            "⚠️ Matn yoki fayl (hujjat, rasm, video, audio, ovozli xabar, GIF, stiker) yuboring, "
            "tugagach 💾 Saqlash bosing. Bekor qilish: /cancel")

    # await'dan oldin qo'shiladi — ketma-ket (albom) yuborilganda tartib saqlanadi
    data["items"].append(item)
    count = len(data["items"])

    old_msg, data["status_msg"] = data["status_msg"], None
    if old_msg:
        try:
            await bot.edit_message_reply_markup(message.chat.id, old_msg, reply_markup=None)
        except Exception:
            pass
    msg = await message.answer(
        f"✅ Qabul qilindi: {_content_summary([(it['type'],) for it in data['items']])}.\n"
        "Yana yuboring yoki 💾 Saqlash bosing.",
        reply_markup=_upload_markup())
    if data["status_msg"] is None and len(data["items"]) == count:
        data["status_msg"] = msg.message_id
    else:
        # shu orada yangi xabar kelgan — tugmalar faqat eng pastdagi xabarda qolsin
        try:
            await msg.edit_reply_markup(reply_markup=None)
        except Exception:
            pass


@dp.callback_query_handler(is_admin, lambda c: bool(c.data) and c.data.startswith("af:"), state="*")
async def panel_save_or_cancel(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    data = _pending.get(user_id)
    action = call.data.split(":")[1]
    try:
        await call.message.edit_reply_markup(reply_markup=None)
    except Exception:
        pass

    in_upload = await state.get_state() == MenuAdmin.kontent.state and data is not None and "items" in data
    if not in_upload:
        await _reset(state, user_id)
        await call.message.answer("Jarayon eskirgan. /menu ni qayta yuboring.", reply_markup=admin_button)
        return await call.answer()
    data["status_msg"] = None
    if action == "cancel":
        await _reset(state, user_id)
        await call.message.answer("❌ Bekor qilindi.", reply_markup=admin_button)
        return await call.answer()

    items = list(data["items"])
    await refresh_menu()
    if data["mode"] == "add":
        # Nom shu orada band bo'lib qolmaganini va joy o'chirilmaganini tekshiramiz
        parent_ok = data["parent"] == ROOT_ID or data["parent"] in _nodes
        if not parent_ok or _validate_name(data["name"], data["parent"], data["kind"]):
            await _reset(state, user_id)
            await call.message.answer(
                "⚠️ Saqlanmadi: bu joy o'chirilgan yoki shu nomli tugma allaqachon bor. /menu ni qayta yuboring.",
                reply_markup=admin_button)
            return await call.answer()
        node_id = await add_node(data["parent"], data["name"], data["kind"], items)
        result = f"💾 Tugma saqlandi!\n\n📍 Joy: {_path(data['parent'])}\n🔘 Tugma: {data['name']}"
    else:
        node_id = data["node"]
        if node_id not in _nodes:
            await _reset(state, user_id)
            await call.message.answer("⚠️ Saqlanmadi: bu tugma o'chirilgan.", reply_markup=admin_button)
            return await call.answer()
        if data["mode"] == "replace":
            await _execute("DELETE FROM menu_files WHERE node_id = ?", (node_id,))
        if items:
            await add_items(node_id, items)
        result = f"💾 Kontent saqlandi!\n\n📍 Tugma: {_path(node_id)}"

    await _reset(state, user_id)
    await refresh_menu()
    await call.message.answer(
        f"{result}\n📎 Qabul qilingan kontent: {_content_summary([(it['type'],) for it in items])}",
        reply_markup=admin_button)
    # Panel yangi tugma ichida ochiladi — darhol uning ichiga tugma qo'shish mumkin
    text, markup = await _panel_view(node_id)
    await call.message.answer(text, reply_markup=markup)
    await call.answer("Saqlandi ✅")
