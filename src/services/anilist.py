from __future__ import annotations

from typing import Any

import aiohttp

_SEARCH_ANIME_QUERY = """
query ($search: String!) {
  Media(search: $search, type: ANIME) {
    id
    title {
      romaji
      english
      native
    }
    status
    episodes
    season
    seasonYear
    coverImage {
      large
    }
  }
}
"""


class AniListClient:
    """Minimal asynchronous client for the AniList GraphQL API."""

    BASE_URL = "https://graphql.anilist.co"

    def __init__(self) -> None:
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self) -> "AniListClient":
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *_: object) -> None:
        if self._session is not None:
            await self._session.close()

    async def _request(
        self,
        query: str,
        variables: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a GraphQL request."""

        if self._session is None:
            raise RuntimeError("AniListClient is not initialized.")

        payload = {
            "query": query,
            "variables": variables or {},
        }

        async with self._session.post(
            self.BASE_URL,
            json=payload,
        ) as response:
            response.raise_for_status()
            return await response.json()

    async def search_anime(self, title: str) -> dict[str, Any]:
        """Search an anime by title."""

        return await self._request(
            query=_SEARCH_ANIME_QUERY,
            variables={
                "search": title,
            },
        )
