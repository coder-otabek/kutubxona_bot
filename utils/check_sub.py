from aiogram import Bot
from typing import List


async def check_subscription_list(bot: Bot, user_id: int, channels: List[str]) -> List[str]:
    unsubscribed = []

    for channel in channels:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)

            if member.status in ['left', 'kicked']:
                unsubscribed.append(channel)

        except Exception as e:
            unsubscribed.append(channel)

    return unsubscribed