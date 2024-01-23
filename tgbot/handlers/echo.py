from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _, SimpleI18nMiddleware
from aiogram.utils.markdown import hcode
from icecream import ic

echo_router = Router()


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message):
    # Assuming you have a translation function (_) set up
    text = [_("Echo without state."), _("Message:"), message.text]

    await message.answer("\n".join(text))


@echo_router.message(F.text)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        _("Echo in state {state_name}").format(state_name=hcode(state_name)),
        _("Message content:"),
        hcode(message.text),
    ]
    await message.answer(_("{text}".format(text="\n".join(text))))
    # await SimpleI18nMiddleware.get_locale()
