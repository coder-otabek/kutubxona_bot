from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from utils.db import Database
import asyncio

from aiogram import types
from loader import dp, bot
from data.config import ADMINS
from filters import IsPrivate

db = Database("main_database.db")


class AdminReklama(StatesGroup):
    reklama_holati = State()
    tasdiqlash_holati = State()


# 1. Admin panel va Statistika
@dp.message_handler(IsPrivate(), text=["Reklama", 'Admin'])
async def admin_panel(message: types.Message):
    if message.from_user.id in ADMINS:
        await db.create_table()
        u_count = await db.count_users()
        g_count = await db.count_groups()  # Guruhlar sonini olish

        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(text="📢 Reklama yuborish", callback_data="reklama_boshlash"),
            types.InlineKeyboardButton(text="🏠 Asosiy menyu", callback_data="back_to_main")
        )
        await message.answer(
            f"📊 <b>Statistika</b>\n\n"
            f"👤 Foydalanuvchilar: {u_count} ta\n"
            f"👥 Guruhlar: {g_count} ta",
            parse_mode='html',
            reply_markup=markup
        )


@dp.callback_query_handler(text="back_to_main", state="*")
async def back_to_main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Asosiy menyuga qaytdingiz")
    try:
        await state.finish()
    except KeyError:
        await state.set_state(None)
    await call.answer()


@dp.callback_query_handler(text="reklama_boshlash", state="*")
async def start_reklama(call: types.CallbackQuery):
    if call.from_user.id in ADMINS:
        await call.message.answer("Reklama xabarini yuboring (Matn, Rasm, Video yoki Post):")
        await AdminReklama.reklama_holati.set()
        await call.answer()


@dp.message_handler(state=AdminReklama.reklama_holati, content_types=types.ContentTypes.ANY)
async def preview_reklama(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(msg_id=message.message_id)

        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(text="✅ Yuborish", callback_data="yuborish_tasdiq"),
            types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="yuborish_bekor")
        )

        await message.answer("<b>Yuqoridagi xabarni barcha foydalanuvchilar va guruhlarga yuborasizmi?</b>",
                             parse_mode='html',
                             reply_markup=markup)
        await AdminReklama.tasdiqlash_holati.set()


@dp.callback_query_handler(text="yuborish_tasdiq", state=AdminReklama.tasdiqlash_holati)
async def confirm_broadcast(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_id = data.get("msg_id")

    users = await db.get_all_users()
    groups = await db.get_all_groups()

    all_targets = users + groups

    count, error = 0, 0
    await call.message.edit_text("🚀 Reklama tarqatilmoqda...")

    for target in all_targets:
        try:
            await bot.copy_message(
                chat_id=target[0],
                from_chat_id=call.from_user.id,
                message_id=msg_id
            )
            count += 1
            await asyncio.sleep(0.05)
        except Exception:
            error += 1

    await call.message.delete()
    await call.message.answer(
        f"✅ <b>Yuborildi:</b> {count}\n❌ <b>Bloklagan/Xato:</b> {error}",
        parse_mode='html',
    )

    try:
        await state.finish()
    except KeyError:
        await state.set_state(None)

    await call.answer()


@dp.callback_query_handler(text="yuborish_bekor", state=AdminReklama.tasdiqlash_holati)
async def cancel_broadcast(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Reklama bekor qilindi.")
    try:
        await state.finish()
    except KeyError:
        await state.set_state(None)

    await call.answer()




@dp.message_handler(IsPrivate(), text="👤 Foydalanuvchilar")
async def show_users_list(message: types.Message):
    if message.from_user.id not in ADMINS:
        return

    users = await db.get_all_users()
    total = len(users)

    if total == 0:
        return await message.answer("Hozircha foydalanuvchi yo‘q.")

    text = [f"Umumiy foydalanuvchilar: <b>{total}</b> ta\n"]

    for u in users:
        user_id = u[0]
        full_name = u[1] if len(u) > 1 else None
        username = u[2] if len(u) > 2 else None

        line = []
        line.append(f"👤 <b>{full_name or 'Noma’lum'}</b>")

        if username:
            line.append(username if str(username).startswith("@") else f"@{username}")
        else:
            line.append(f"🆔 <code>{user_id}</code>")

        text.append("\n".join(line))
        text.append("—")

    out = "\n".join(text)
    if len(out) <= 3500:
        await message.answer(out, parse_mode="HTML")
    else:
        chunk = ""
        for part in text:
            if len(chunk) + len(part) + 1 > 3500:
                await message.answer(chunk, parse_mode="HTML")
                chunk = ""
            chunk += part + "\n"
        if chunk.strip():
            await message.answer(chunk, parse_mode="HTML")
@dp.message_handler(IsPrivate(), text="👥 Guruhlar")
async def show_groups_list(message: types.Message):
    if message.from_user.id not in ADMINS:
        return

    groups = await db.get_all_groups()
    total = len(groups)

    if total == 0:
        return await message.answer("Hozircha guruh yo‘q.")

    text = [f"Umumiy guruhlar: <b>{total}</b> ta\n"]

    for g in groups:
        group_id = g[0]
        title = g[1] if len(g) > 1 else None
        group_username = g[2] if len(g) > 2 else None  # ✅ username
        link = g[3] if len(g) > 3 else None            # ✅ link

        text.append(f"👥 <b>{title or 'Noma’lum guruh'}</b>")

        if link:
            text.append(f"🔗 {link}")
        elif group_username:
            gu = group_username[1:] if str(group_username).startswith("@") else group_username
            text.append(f"🔗 https://t.me/{gu}")
        else:
            text.append(f"ID: <code>{group_id}</code>")

        text.append("—")

    out = "\n".join(text)
    if len(out) <= 3500:
        await message.answer(out, parse_mode="HTML")
    else:
        chunk = ""
        for part in text:
            if len(chunk) + len(part) + 1 > 3500:
                await message.answer(chunk, parse_mode="HTML")
                chunk = ""
            chunk += part + "\n"
        if chunk.strip():
            await message.answer(chunk, parse_mode="HTML")
