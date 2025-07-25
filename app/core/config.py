"""Configuration module for application settings using Pydantic."""

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """
    Defines the application's configuration settings.
    Pydantic will automatically look for matching environment variables.
    """
    openai_api_key: str

    verbose: Optional[bool] = False

    model_config = SettingsConfigDict(env_file=".env")


# Only initialize settings if we're not in a documentation build context
_settings = None

def get_settings() -> Settings:
    """Get settings instance, initializing if needed."""
    global _settings
    if _settings is None:
        # During docs build or when no env vars are available, use a mock settings object
        try:
            _settings = Settings()
        except Exception:
            # Create a mock settings object for docs or when env vars are missing
            class MockSettings:
                openai_api_key = "dummy_key_for_docs"
                verbose = False
            _settings = MockSettings()
    return _settings
