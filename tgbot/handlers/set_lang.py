import locale

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _, SimpleI18nMiddleware

set_lang = Router()


@set_lang.message(Command('uz', 'ru', 'en'))
async def user_start(message: Message):
    await message.answer('kuting')

    # Update the user's locale in user_data
    message.from_user['locale'] = message.text

    await message.answer(f"Language set to {locale}")
