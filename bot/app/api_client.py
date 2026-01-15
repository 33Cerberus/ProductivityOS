import requests

BACKEND_URL = "http://127.0.0.1:8000"

def create_user(user_id: int, timezone: str) -> dict:
    response = requests.post(
        f"{BACKEND_URL}/users",
        json={"id": user_id, "timezone": timezone},
        timeout=5
    )
    response.raise_for_status()
    return response.json()

def get_user(user_id: int) -> dict:
    response = requests.get(f"{BACKEND_URL}/users/{user_id}", timeout=5)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()

def get_users() -> list:
    response = requests.get(f"{BACKEND_URL}/users", timeout=5)
    response.raise_for_status()
    return response.json()

def update_user(user_id: int, timezone: str) -> dict:
    response = requests.put(
        f"{BACKEND_URL}/users/{user_id}",
        json={"timezone": timezone},
        timeout=5
    )
    response.raise_for_status()
    return response.json()