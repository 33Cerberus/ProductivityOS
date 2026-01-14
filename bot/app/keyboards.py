from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.timezone import REGION_CITIES

add_task_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Add task")]], resize_keyboard=True)

def tz_guess(tz):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Confirm", callback_data=f"confirm_tz:{tz}"))
    keyboard.add(InlineKeyboardButton(text="Change", callback_data="change_tz_guess"))
    return keyboard.adjust(2).as_markup()

regions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Europe", callback_data="region:europe")],
    [InlineKeyboardButton(text="Americas", callback_data="region:americas")],
    [InlineKeyboardButton(text="Asia", callback_data="region:asia")],
    [InlineKeyboardButton(text="Africa", callback_data="region:africa")],
    [InlineKeyboardButton(text="Australia / Oceania", callback_data="region:oceania")],
])


def region_cities(region: str) -> InlineKeyboardBuilder:
    cities = REGION_CITIES.get(region.lower())
    if not cities:
        raise ValueError(f"Unknown region: {region}")

    keyboard = InlineKeyboardBuilder()

    for tz_name in cities:
        offset_sec = datetime.now(ZoneInfo(tz_name)).utcoffset().total_seconds()
        offset_hours = int(offset_sec // 3600)
        offset_minutes = int((offset_sec % 3600) // 60)
        if offset_minutes:
            offset_str = f"UTC{offset_hours:+d}:{offset_minutes:02d}"
        else:
            offset_str = f"UTC{offset_hours:+d}"

        city_display = f"{tz_name.split('/')[-1].replace('_', ' ')} ({offset_str})"
        keyboard.add(InlineKeyboardButton(
            text=city_display,
            callback_data=f"confirm_tz:{tz_name}"
        ))

    keyboard.add(InlineKeyboardButton(
        text="Back",
        callback_data=f"back"
    ))

    return keyboard.adjust(2).as_markup()