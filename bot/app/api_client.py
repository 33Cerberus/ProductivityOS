import requests
from datetime import datetime

BACKEND_URL = "http://127.0.0.1:8000"

def register_user(user_id: int, timezone: str, created_at: datetime) -> dict:
    response = requests.post(
        f"{BACKEND_URL}/register",
        json={
            "id": user_id,
            "timezone": timezone,
            "created_at": created_at.isoformat(),
        },
        timeout=5
    )

    response.raise_for_status()

    return response.json()
