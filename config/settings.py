from pydantic import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    telegram_webhook_secret: str = "dev"

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
