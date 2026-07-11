from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

VALID_ENVIRONMENTS = {"development", "staging", "production"}


@dataclass(frozen=True)
class Settings:
    environment: str
    discord_token: str
    database_url: str
    log_level: str

    @classmethod
    def from_env(cls, *, require_token: bool = False) -> "Settings":
        load_dotenv()

        environment = os.getenv("APP_ENV", "development").lower()
        if environment not in VALID_ENVIRONMENTS:
            valid = ", ".join(sorted(VALID_ENVIRONMENTS))
            raise ValueError(f"APP_ENV must be one of: {valid}")

        discord_token = os.getenv("DISCORD_TOKEN", "")
        if require_token and not discord_token:
            raise ValueError("DISCORD_TOKEN is not configured.")

        database_url = os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:postgres@localhost:5432/anime_notify",
        )

        return cls(
            environment=environment,
            discord_token=discord_token,
            database_url=database_url,
            log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
        )


settings = Settings.from_env()
