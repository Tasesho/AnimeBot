from __future__ import annotations

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class User(Base):
    """Discord user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
    )