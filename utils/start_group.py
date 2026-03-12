from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from filters import IsGroup
from loader import dp
from utils.db import Database

db = Database("main_database.db")


@dp.message_handler(IsGroup(), CommandStart())
async def start_group(message: types.Message):
    await db.create_table()

    await db.add_group(
        group_id=message.chat.id,
        title=message.chat.title
    )

    text = (
        f"📚 Assalomu alaykum, <b>{message.chat.title}</b> a'zolari!!!\n\n"
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