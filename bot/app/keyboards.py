from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

add_task_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Add task")]], resize_keyboard=True)