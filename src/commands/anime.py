from __future__ import annotations

import logging

import discord
from discord import app_commands
from discord.ext import commands

from models.anime import Anime

logger = logging.getLogger(__name__)


class AnimeCog(commands.Cog):
    """Anime related commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name="search",
        description="Search an anime using AniList",
    )
    async def search(
        self,
        interaction: discord.Interaction,
        title: str,
    ) -> None:
        """Search an anime."""

        logger.info(
            "User %s (%s) searched for %s",
            interaction.user,
            interaction.user.id,
            title,
        )

        await interaction.response.defer()

        anime: Anime | None = await self.bot.anilist.search_anime(title)

        if anime is None:
            await interaction.followup.send("Anime not found.")
            return

        embed = discord.Embed(
            title=anime.title,
            description="Anime information from AniList",
        )

        embed.add_field(
            name="Status",
            value=anime.status,
            inline=True,
        )

        embed.add_field(
            name="Episodes",
            value=str(anime.episodes or "Unknown"),
            inline=True,
        )

        if anime.cover_image:
            embed.set_thumbnail(
                url=anime.cover_image,
            )

        await interaction.followup.send(
            embed=embed,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AnimeCog(bot))
