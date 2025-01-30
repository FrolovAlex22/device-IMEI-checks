import logging

from aiogram import F, Router
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove, Contact

from filters.users_whitelist import IsWhitelist
from lexicon.lexicon import LEXICON_USER


user_router = Router()
user_router.message.filter(IsWhitelist())

logger = logging.getLogger(__name__)


@user_router.message(CommandStart())
async def start_cmd(message: Message):
    """Сообщение в случае команды /start"""
    logger.info(f"Пользователь {message.from_user.id} запустил бота")

    await message.answer(
        LEXICON_USER["start_button"],
        reply_markup=None
    )
