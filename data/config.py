import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env.shablon.shablon faylida topilmadi!")

# ✅ ADMINS ni to'g'ri parse qilish
ADMINS = os.getenv("ADMINS", "")

ADMINS = [int(admin.strip()) for admin in ADMINS.split(",") if admin.strip()]
