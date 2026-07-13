from __future__ import annotations

import logging

import discord
from discord.ext import commands

from config import settings
from services.anilist import AniListClient

logging.basicConfig(
    level=settings.log_level,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


class AnimeNotifyBot(commands.Bot):
    """Main Discord bot instance."""

    def __init__(self) -> None:
        intents = discord.Intents.default()

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

        self.anilist = AniListClient()

    async def setup_hook(self) -> None:
        """Initialize services before the bot starts."""

        await self.anilist.__aenter__()

        await self.load_extension("commands.anime")

    async def close(self) -> None:
        """Cleanup resources before shutting down."""

        await self.anilist.__aexit__(None, None, None)

        await super().close()


bot = AnimeNotifyBot()


@bot.event
async def on_ready() -> None:
    logger.info(
        "Logged in as %s (%s)",
        bot.user,
        bot.user.id,
    )


def main() -> None:
    logger.info("Starting Anime Notify...")
    bot.run(
        settings.discord_token,
        log_handler=None,
    )


if __name__ == "__main__":
    main()