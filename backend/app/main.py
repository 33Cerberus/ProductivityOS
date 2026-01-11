from fastapi import FastAPI
from backend.app.api.users import router as users_router
from backend.app.database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(users_router)
