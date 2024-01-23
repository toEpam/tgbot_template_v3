from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message

import bot

docs_router = Router()

# kelgan hujjatlar (rasm/video/audio...) downloads/categories papkasiga tushadi
download_path = Path().joinpath("downloads","categories")
download_path.mkdir(parents=True, exist_ok=True)

@docs_router.message(F.text)
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")

@docs_router.message(F.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    # file_id = message.document.file_id
    # file = await bot.get_file(file_id)
    # file_path = file.file_path
    document = message.document
    await bot.download(document)
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {document.file_id}")

# @docs_router.message(F.VIDEO)
@docs_router.message(F.video)
async def video_handler(message: Message):
    # await message.video.download(destination=download_path)
    await message.reply("Video qabul qilindi\n"
                    f"file_id = {message.video.file_id}")

@docs_router.message(F.photo)
async def video_handler(message: Message):
    # await message.photo[-1].download(destination=download_path)
    await message.reply("Rasm qabul qilindi\n"
                    f"file_id = {message.photo[-1].file_id}")

# Bu yerga yuqoridagi 3 turdan boshqa barcha kontentlar tushadi
@docs_router.message()
async def any_handler(message: Message):
    await message.reply(f"{message.content_type.split('.')[-1]} qabul qilindi")

# https://docs.aiogram.dev/en/latest/api/download_file.html