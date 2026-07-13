from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Anime:
    """Represents an anime returned by the AniList API."""

    id: int
    title: str
    status: str
    episodes: int | None
    season: str | None
    season_year: int | None
    cover_image: str | None