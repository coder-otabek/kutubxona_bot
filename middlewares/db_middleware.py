from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.db import Database

db = Database("main_database.db")


class DbMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        # Ba'zi update'larda from_user bo'lmay qolishi mumkin (kamdan-kam)
        if not message.from_user:
            return

        user_id = message.from_user.id
        full_name = message.from_user.full_name
        # username = message.from_user.username  # None bo‘lishi mumkin

        # 1) user bazada bormi?
        user = await db.get_user(user_id)

        # user yo‘q bo‘lsa — qo‘shib qo‘yamiz
        if not user:
            await db.add_user(user_id=user_id, name=full_name)
            return

        # 2) user bo‘lsa — faqat o‘zgargan bo‘lsa update qilamiz
        # user tuple: (user_id, name, email, contact)
        old_name = user[1]

        if old_name != full_name:
            await db.update_user_name(
                user_id=user_id,
                name=full_name
            )
