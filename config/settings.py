from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    telegram_bot_token: str
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
