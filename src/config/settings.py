from pydantic import BaseSettings, Field
from config.metaclasses import Singleton


class Settings(BaseSettings):
    __metaclass__ = Singleton

    db_name: str = Field(env="DB_NAME")
    db_host: str = Field(env="DB_HOST")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")

    def get_db_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432/{self.db_name}"

    class Config:
        env_file = ".env"


settings = Settings()
