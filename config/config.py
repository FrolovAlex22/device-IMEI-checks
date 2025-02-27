import os
from dataclasses import dataclass

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_IDS = [int(i) for i in os.getenv('ADMIN_IDS').split(',')]
IMEI_TOKEN = os.getenv('IMEI_TOKEN')
URL = os.getenv('URL')


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config() -> Config:
    return Config(
        tg_bot=TgBot(
            token=BOT_TOKEN,
            admin_ids=list(ADMIN_IDS)
        ),
    )
