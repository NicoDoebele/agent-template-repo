"""Configuration module for application settings using Pydantic."""

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Defines the application's configuration settings.
    Pydantic will automatically look for matching environment variables.
    """
    openai_api_key: str
    model_name: str = "gpt-4o"

    verbose: Optional[bool] = False

    model_config = SettingsConfigDict(env_file=".env")


def get_settings() -> Settings:
    """Get settings instance."""
    try:
        return Settings()
    except (ValueError, TypeError):
        # Create a mock settings object for docs
        # or when env vars are missing
        class MockSettings:  # pylint: disable=too-few-public-methods
            """Mock settings for documentation builds."""
            openai_api_key = "dummy_key_for_docs"
            model_name = "gpt-4o"
            verbose = False

        return MockSettings()
