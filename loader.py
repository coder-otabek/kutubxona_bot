from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from middlewares.throttling import ThrottlingMiddleware
from data.config import BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
user_ids = set()

# Middleware ulash
dp.middleware.setup(ThrottlingMiddleware())
