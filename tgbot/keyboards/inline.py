from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def aiogram_keys_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Kursni boshlash", url="https://mohirdev.uz/courses/telegram"),
        InlineKeyboardButton(text="Batafsil", callback_data="course:aiogram")
    )
    keyboard.row(InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="kurs"))
    return keyboard.as_markup()


def python_keys_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text="Kursni boshlash", url="https://mohirdev.uz/courses/python"),
        InlineKeyboardButton(text="Batafsil", callback_data="course:python")
    )
    keyboard.row(InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="kurs"))
    return keyboard.as_markup()
