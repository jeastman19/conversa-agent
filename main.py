from fastapi import FastAPI, Request
from adapters.inbound.telegram_bot import handle_telegram_webhook
from config.settings import get_settings

app = FastAPI()
settings = get_settings()


@app.post("/webhook/telegram")
async def telegram_webhook(request: Request):
    payload = await request.json()
    await handle_telegram_webhook(payload)
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok"}
