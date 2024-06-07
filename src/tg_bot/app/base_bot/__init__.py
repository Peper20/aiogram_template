from aiogram import Dispatcher

from .handlers import router


async def init(dp: Dispatcher):
    dp.include_router(router)