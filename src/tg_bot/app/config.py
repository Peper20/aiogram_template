import tomllib

from dataclasses import dataclass
from dishka import provide, Provider, Scope




@dataclass(frozen=True, slots=True, kw_only=True)
class DatabaseConfig:
    user: str
    password: str
    host: str
    name: str

    @property
    def url(self):
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}'


@dataclass(frozen=True, slots=True, kw_only=True)
class TgBotConfig:
    token: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    database_config: DatabaseConfig
    tg_bot_config: TgBotConfig


class ConfigProvider(Provider):
    scope = Scope.APP


    @provide
    def get_config(self) -> Config:
        with open('config.toml', 'rb') as f:
            _config_data = tomllib.load(f)
        
        return Config(
            database_config=DatabaseConfig(**_config_data['database']),
            tg_bot_config=TgBotConfig(**_config_data['tg_bot']),
        )

    @provide
    def get_database_config(self, config: Config) -> DatabaseConfig:
        return config.database_config

    @provide
    def get_tg_bot_config(self, config: Config) -> TgBotConfig:
        return config.tg_bot_config

