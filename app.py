from aiogram import executor

from middlewares.db_middleware import DbMiddleware
from loader import dp
from utils.db import Database

DB_PATH = "main_database.db"
db = Database(DB_PATH)


# =====================================================================
#  Handlerlar (dinamik menyu handlers.users ichida birinchi bo'lib ulanadi)
# =====================================================================
import middlewares, filters, handlers
from handlers.users.dynamic_menu import refresh_menu
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # ✅ 1) DB tablelarni yaratib olamiz (users, groups)
    await db.create_table()

    # ✅ Dinamik menyu jadvallari va asosiy menyudagi yangi tugmalar
    await refresh_menu()

    # ✅ 2) Middleware'ni shu yerda ulash ham xavfsizroq
    dispatcher.middleware.setup(DbMiddleware())

    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
