from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncpg

from tgbot import config

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer("Greetings, regular user!")

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=config.tg_bot.admin_ids[0], text=msg)

@user_router.message_handler(text="/reklama", user_id=config.tg_bot.admin_ids)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        await bot.send_message(chat_id=user_id, text="@SariqDev kanaliga obuna bo'ling!")
        await asyncio.sleep(0.05)