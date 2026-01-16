from typing import Optional
from datetime import date as date_type
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

async def create_task(user_id: int, date: date_type, description: str) -> dict:
    async with session.post(f"{BACKEND_URL}/tasks",json={"user_id": user_id, "date": date.isoformat(), "description": description}) as response:
        response.raise_for_status()
        return await response.json()

async def get_task(task_id: int) -> dict:
    async with session.get(f"{BACKEND_URL}/tasks/{task_id}") as response:
        if response.status == 404:
            return None
        response.raise_for_status()
        return await response.json()

async def get_tasks(user_id: Optional[int] = None) -> list:
    async with session.get(f"{BACKEND_URL}/tasks", json={"user_id": user_id}) as response:
        response.raise_for_status()
        return await response.json()

async def update_task(task_id: int, completed: Optional[bool], date: Optional[date_type], description: Optional[str]) -> dict:
    async with session.put(f"{BACKEND_URL}/tasks/{task_id}", json={"completed": completed, "date": date.isoformat(), "description": description}) as response:
        response.raise_for_status()
        return await response.json()