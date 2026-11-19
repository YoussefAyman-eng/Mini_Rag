from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    App_name: str = "Mini-Rag"
    App_version: str = "0.1"
    Open_ai_api_key: str = ""
    File_max_size: int = 10
    File_allowed_extensions: list[str] = [".txt", ".pdf", ".docx"]

    class Config:
        env_file = ".env"
       
    def get_settings(self):
        return {
            "app_name": self.App_name,
            "app_version": self.App_version,
            "open_ai_api_key": self.Open_ai_api_key,
            "file_max_size": self.File_max_size,
            "file_allowed_extensions": self.File_allowed_extensions
        }

@lru_cache()
def get_settings():
    return Settings()