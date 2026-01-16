from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "db.sqlite3"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

print("🔥 DATABASE FILE:", DATABASE_PATH)