from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "support-chatbot"
    VECTOR_STORE_PATH: str = "data/vector_store"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
