from aiogram import Bot, Dispatcher


from .features import features
from .settings import tg_bot_config




async def create_app() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=tg_bot_config.token)
    dp = Dispatcher()

    for feature in features:
        if hasattr(feature, 'init'):
            await feature.init(dp)

    return bot, dp


async def start_app() -> None:
    bot, dp = await create_app()
    await dp.start_polling(bot)

