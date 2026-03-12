from aiogram import executor
from middlewares.db_middleware import DbMiddleware
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db import Database

db = Database("main_database.db")


async def on_startup(dispatcher):
    # ✅ 1) DB tablelarni yaratib olamiz (users, groups)
    await db.create_table()

    # ✅ 2) Middleware'ni shu yerda ulash ham xavfsizroq
    dispatcher.middleware.setup(DbMiddleware())

    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
