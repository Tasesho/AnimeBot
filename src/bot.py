from __future__ import annotations

import logging

import discord
from discord.ext import commands

from config import settings


logging.basicConfig(
    level=settings.log_level,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)


@bot.event
async def on_ready() -> None:
    logger.info("Logged in as %s (%s)", bot.user, bot.user.id)


def main() -> None:
    logger.info("Starting Anime Notify...")
    bot.run(settings.discord_token, log_handler=None)


if __name__ == "__main__":
    main()