import asyncio
from aiogram import Bot, Dispatcher
from bot.app.api_client import init_session, close_session
from config import BOT_TOKEN

from bot.app.handlers import router

async def on_startup():
    await init_session()

async def on_shutdown():
    await close_session()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stopping...')