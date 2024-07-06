from aiogram import Router, F, types, html
from aiogram.types import Message
from aiogram.filters.command import Command
from dishka import FromDishka




router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer(html.quote('Hello!'))
