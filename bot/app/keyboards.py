from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.timezone import REGION_CITIES, format_tz_offset


def tz_guess(tz: str) -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Confirm", callback_data=f"confirm_tz:{tz}"))
    keyboard.add(InlineKeyboardButton(text="Change", callback_data="change_tz_guess"))
    return keyboard.adjust(2).as_markup()

def regions() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()
    for region in REGION_CITIES.keys():
        display_name = region.capitalize()
        keyboard.add(InlineKeyboardButton(text=display_name, callback_data=f"region:{region}"))
    keyboard.add(InlineKeyboardButton(text="Back", callback_data="back:start"))
    return keyboard.adjust(2).as_markup()


def region_cities(region: str) -> InlineKeyboardBuilder:
    cities = REGION_CITIES.get(region.lower())
    if not cities:
        raise ValueError(f"Unknown region: {region}")

    keyboard = InlineKeyboardBuilder()
    for tz_name in cities:
        offset_str = format_tz_offset(tz_name)
        city_display = f"{tz_name.split('/')[-1].replace('_', ' ')} ({offset_str})"
        keyboard.add(InlineKeyboardButton(
            text=city_display,
            callback_data=f"confirm_tz:{tz_name}"
        ))
    keyboard.add(InlineKeyboardButton(text="Back", callback_data="back:regions"))
    return keyboard.adjust(2).as_markup()
