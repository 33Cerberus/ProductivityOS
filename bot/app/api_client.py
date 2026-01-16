from typing import Optional
import aiohttp
from aiohttp import ClientSession
from config import BACKEND_URL

session: Optional[ClientSession] = None

async def init_session():
    global session
    session = aiohttp.ClientSession()

async def close_session():
    if session:
        await session.close()

async def create_user(user_id: int, timezone: str) -> dict:
    async with session.post(f"{BACKEND_URL}/users",json={"id": user_id, "timezone": timezone}) as response:
        response.raise_for_status()
        return await response.json()

async def get_user(user_id: int) -> dict:
    async with session.get(f"{BACKEND_URL}/users/{user_id}") as response:
        if response.status == 404:
            return None
        response.raise_for_status()
        return await response.json()

async def get_users() -> list:
    async with session.get(f"{BACKEND_URL}/users") as response:
        response.raise_for_status()
        return await response.json()

async def update_user(user_id: int, timezone: str) -> dict:
    async with session.put(f"{BACKEND_URL}/users/{user_id}", json={"timezone": timezone}) as response:
        response.raise_for_status()
        return await response.json()