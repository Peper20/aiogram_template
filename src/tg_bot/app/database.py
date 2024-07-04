from typing import AsyncGenerator
from dishka import provide, provide_all, Provider, Scope
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine


from app.config import DatabaseConfig




class DatabaseProvider(Provider):
    _engine: AsyncEngine = None
    _session_maker: async_sessionmaker = None

    scope = Scope.REQUEST
    repos = provide_all()


    def __init__(self, config: DatabaseConfig):
        super().__init__()
        self._engine = create_async_engine(config.url)
        self._session_maker = async_sessionmaker(self._engine, expire_on_commit=False)


    @provide
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_maker() as session:
            yield session

