from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

class AdminFilter(BoundFilter):
    async def check(self, message: Message) -> bool:
        if message.chat.type not in ("group", "supergroup"):
            return False

        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.status in ("administrator", "creator")
