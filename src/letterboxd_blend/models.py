"""Core data models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True)
class Movie:
    """A film, identified by its Letterboxd URI."""

    uri: str
    name: str
    year: int | None = None


@dataclass(frozen=True)
class DiaryEntry:
    """A single diary log: when a movie was watched and how it was rated."""

    movie: Movie
    watched_on: date | None = None
    rating: float | None = None  # 0.5 - 5.0 in half-star steps
    rewatch: bool = False
    tags: tuple[str, ...] = ()


@dataclass
class Profile:
    """Everything we know about one person's taste."""

    username: str
    watched: set[Movie] = field(default_factory=set)
    ratings: dict[Movie, float] = field(default_factory=dict)
    diary: list[DiaryEntry] = field(default_factory=list)


@dataclass(frozen=True)
class Recommendation:
    """A movie both people are likely to enjoy, with an explanation."""

    movie: Movie
    score: float
    reason: str = ""
