from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""

    LLM_PROVIDER: str = "openai"

    OPENAI_MODEL: str = "gpt-5"

    OLLAMA_MODEL: str = "llama3.1:8b"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()