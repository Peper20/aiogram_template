import tomllib

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class DbConfig:
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


with open("config.toml", "rb") as f:
    _config_data = tomllib.load(f)


db_config = DbConfig(**_config_data['db'])
tg_bot_config = TgBotConfig(**_config_data['tg_bot'])