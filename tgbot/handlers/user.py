from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply(_("Greetings, regular user!"))
