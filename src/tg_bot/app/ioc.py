from aiogram import Dispatcher
from dishka.integrations.aiogram import setup_dishka
from dishka import AsyncContainer, make_async_container


from app.config import ConfigProvider




async def setup(container: AsyncContainer, dp: Dispatcher) -> None:
    setup_dishka(container=container, router=dp, auto_inject=True)


async def create_container() -> AsyncContainer:
    config = ConfigProvider()

    return make_async_container(config)


