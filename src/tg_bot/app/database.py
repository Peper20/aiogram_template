from typing import AsyncGenerator
from dishka import provide, provide_all, Provider, Scope
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine


from app.config import DatabaseConfig




class DatabaseProvider(Provider):
    _config: DatabaseConfig = None
    repos = provide_all(scope=Scope.REQUEST)


    def __init__(self, config: DatabaseConfig):
        super().__init__()
        self._config = config


    @provide(scope=Scope.APP)
    async def engine(self) -> AsyncEngine:
        return create_async_engine(self._config.url)
    

    @provide(scope=Scope.REQUEST)
    async def session(self, engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
        async with AsyncSession(engine) as session:
            yield session

