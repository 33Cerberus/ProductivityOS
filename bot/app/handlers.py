from datetime import datetime
from zoneinfo import ZoneInfo
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from bot.app.api_client import register_user
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import tz_guess, regions, region_cities
from utils.timezone import guess_timezone_from_language

router = Router()

API_URL = "http://127.0.0.1:8000"

class TimezoneSelection(StatesGroup):
    region_selection = State()
    city_selection = State()

@router.message(CommandStart())
async def handle_start(message: Message):
    tz = guess_timezone_from_language(message.from_user.language_code)
    await message.answer(f"Welcome to *ProductivityOS*!\n\n"
                         f"To work correctly, the bot needs to know your time zone.\n\n"
                         f"It looks like *{tz}*\n\n"
                         f"Is it correct?", reply_markup=tz_guess(tz), parse_mode="Markdown")

@router.callback_query(F.data.startswith("confirm_tz:"))
async def handle_confirm_tz(callback: CallbackQuery):
    tz = callback.data.split(":")[1]
    register_user(
        user_id=callback.message.from_user.id,
        timezone=tz,
        created_at=datetime.now(ZoneInfo(tz)))
    await callback.message.answer(f"Timezone successfully selected!\n\nYou can change it anytime, using corresponding button")
    await callback.answer()

@router.callback_query(F.data == "change_tz_guess")
async def handle_change_tz(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TimezoneSelection.region_selection)
    await callback.message.answer("Select your region", reply_markup=regions)
    await callback.answer()

@router.callback_query(F.data.startswith("region:"))
async def handle_region(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TimezoneSelection.city_selection)
    region = callback.data.split(":")[1]
    await callback.message.edit_text("Select your city", reply_markup=region_cities(region))
    await callback.answer()
