from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from bot.app.api_client import create_user, get_user, update_user, create_task, get_task, update_task, get_task
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from keyboards import tz_guess, regions, region_cities
from utils.timezone import guess_timezone_from_language
from datetime import date as date_type

router = Router()

class TimezoneSelection(StatesGroup):
    tz_confirmation_or_change = State()
    region_selection = State()

async def send_start_message(message: Message, state: FSMContext):
    saved_data = await state.get_data()
    saved_tz = saved_data.get("guessed_tz")
    saved_msg = saved_data.get("start_msg")
    tz = saved_tz if saved_tz else guess_timezone_from_language(message.from_user.language_code)
    await state.set_state(TimezoneSelection.tz_confirmation_or_change)
    text = (f"Welcome to *ProductivityOS*!\n\n"
            f"To work correctly, the bot needs to know your time zone.\n\n"
            f"It looks like *{tz}*\n\n"
            f"Is it correct?")
    if saved_msg:
        await saved_msg.edit_text(text, reply_markup=tz_guess(tz), parse_mode="Markdown")
    else:
        msg = await message.answer(text, reply_markup=tz_guess(tz), parse_mode="Markdown")
        await state.update_data(guessed_tz=tz, start_msg=msg)

@router.message(CommandStart())
async def handle_start(message: Message, state: FSMContext):
    await send_start_message(message, state)

@router.callback_query(TimezoneSelection.tz_confirmation_or_change, F.data.startswith("confirm_tz:"))
async def handle_confirm_tz(callback: CallbackQuery, state: FSMContext):
    tz = callback.data.split(":")[1]
    user = await get_user(callback.from_user.id)

    if user is None:
        await create_user(user_id=callback.from_user.id, timezone=tz)
    else:
        await update_user(user_id=callback.from_user.id, timezone=tz)

    await state.clear()
    await callback.message.edit_text(
        f"Timezone *{tz}* successfully selected!\n\nYou can change it anytime, using corresponding button",
        parse_mode="Markdown")
    await callback.answer()

@router.callback_query(TimezoneSelection.tz_confirmation_or_change, F.data == "change_tz_guess")
async def handle_change_tz(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TimezoneSelection.region_selection)
    await callback.message.edit_text("Select your region", reply_markup=regions())
    await callback.answer()

@router.callback_query(TimezoneSelection.region_selection, F.data.startswith("region:"))
async def handle_region(callback: CallbackQuery, state: FSMContext):
    region = callback.data.split(":")[1]
    await state.set_state(TimezoneSelection.tz_confirmation_or_change)
    await callback.message.edit_text("Select your city", reply_markup=region_cities(region))
    await callback.answer()

@router.callback_query(F.data.startswith("back:"))
async def handle_back(callback: CallbackQuery, state: FSMContext):
    back_to = callback.data.split(":")[1]
    match back_to:
        case "start":
            await state.set_state(None)
            await send_start_message(callback.message, state)
        case "regions":
            await state.set_state(TimezoneSelection.region_selection)
            await callback.message.edit_text("Select your region", reply_markup=regions())
    await callback.answer()

@router.message(F.text == "/add")
async def handle_add(message: Message, state: FSMContext):
    await create_task(message.from_user.id, date_type.today(), "test task")