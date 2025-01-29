import logging

from aiogram import F, Router
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove, Contact


other_router = Router()

logger = logging.getLogger(__name__)