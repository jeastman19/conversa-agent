from fastapi import FastAPI
from app.adapters.telegram import routes as telegram_routes

app = FastAPI()
app.include_router(telegram_routes.router)
