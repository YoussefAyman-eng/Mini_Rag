from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Mini-Rag"
    app_version: str = "0.1"
    open_ai_api_key: str = ""
    file_max_size: int = 10
    file_allowed_extensions: list[str] = [".txt", ".pdf", ".docx"]

    def get_settings(self):
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "open_ai_api_key": self.open_ai_api_key,
            "file_max_size": self.file_max_size,
            "file_allowed_extensions": self.file_allowed_extensions
        }