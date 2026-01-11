from datetime import datetime
from zoneinfo import ZoneInfo
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.app.api_client import register_user

router = Router()

API_URL = "http://127.0.0.1:8000"


@router.message(CommandStart())
async def handle_start(message: Message):
    try:
        user = register_user(
            user_id=message.from_user.id,
            timezone="Europe/Warsaw",
            created_at=datetime.now(ZoneInfo("Europe/Warsaw")),
        )
    except Exception:
        await message.answer("Bot error")
        return

    await message.answer("User registered successfully")
