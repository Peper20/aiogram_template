from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters.command import Command




router = Router()


@router.message(Command('start'))
async def message_with_text(message: Message):
    await message.answer('Hello!')


