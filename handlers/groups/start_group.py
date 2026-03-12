from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from filters import IsGroup
from loader import dp, bot
from utils.db import Database

db = Database("main_database.db")


@dp.message_handler(IsGroup(), CommandStart())
async def start_group(message: types.Message):
    # ✅ tablelar borligini kafolatlaymiz
    await db.create_table()

    chat = message.chat
    group_username = chat.username  # public bo‘lsa bor, private bo‘lsa None

    # ✅ public bo‘lsa: t.me/username link
    group_link = f"https://t.me/{group_username}" if group_username else None

    # ✅ private guruhlar uchun invite link olishga urinib ko‘ramiz
    # (bot admin bo‘lsa va invite link export ruxsati bo‘lsa ishlaydi)
    if group_link is None:
        try:
            group_link = await bot.export_chat_invite_link(chat.id)
        except Exception:
            group_link = None

    await db.add_group(
        group_id=chat.id,
        title=chat.title,
        username=group_username,
        link=group_link
    )

    text = (
        f"📚 Assalomu alaykum, <b>{chat.title}</b> a'zolari!!!\n\n"
        "Bu guruh bilan birga bizda <b>Online Kutubxona</b> ham mavjud 📖\n\n"
        "🔹 Minglab elektron kitoblar\n"
        "🔹 Tez va qulay qidiruv\n"
        "🔹 24/7 foydalanish\n\n"
        "👉 <a href='https://t.me/E_KitobXazinasi_Bot'>Kutubxonaga o‘tish uchun bosing</a>"
    )
    await message.answer(text, parse_mode="html", disable_web_page_preview=True)


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    text = "Yordam kerak bo'lsa adminga murojaat qiling!\n👉 https://t.me/abdumalikovotabek2006"
    await message.answer(text)
