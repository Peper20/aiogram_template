import logging; logging.basicConfig(level=logging.INFO)


from aiogram import Bot, Dispatcher


from app.features import features
from app.config import TgBotConfig
from app.ioc import create_container, setup




async def create_app() -> tuple[Bot, Dispatcher]:
    container = await create_container()

    dp = Dispatcher()
    bot = Bot(
        token=(await container.get(TgBotConfig)).token,
        parse_mode='html',
    )

    for feature in features:
        if hasattr(feature, 'init'):
            await feature.init(dp)

    await setup(container, dp)

    return bot, dp


async def start_app() -> None:
    bot, dp = await create_app()
    await dp.start_polling(bot)

