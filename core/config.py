"""
Application configuration.

Loads all settings from the .env file and provides
a single source of truth for the application.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    LLM_PROVIDER: str = "openai"

    OPENAI_API_KEY: str = ""

    OPENAI_MODEL: str = "gpt-5"

    OLLAMA_MODEL: str = "qwen2.5:7b"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()