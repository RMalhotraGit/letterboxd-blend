"""The blend algorithm: find movies two people would both like."""

from __future__ import annotations

from .models import Movie, Profile, Recommendation


def shared_taste(a: Profile, b: Profile) -> float:
    """Return a 0-1 similarity score between two profiles.

    TODO: e.g. rating correlation over movies both have rated.
    """
    raise NotImplementedError


def candidates(a: Profile, b: Profile, catalog: set[Movie]) -> set[Movie]:
    """Movies neither person has watched yet, drawn from ``catalog``."""
    return catalog - a.watched - b.watched


def blend(
    a: Profile,
    b: Profile,
    catalog: set[Movie],
    top_n: int = 10,
) -> list[Recommendation]:
    """Recommend up to ``top_n`` unseen movies that both people would likely enjoy.

    TODO: predict each person's rating per candidate, then combine
    (e.g. mean, or min to penalize movies one person would dislike).
    """
    raise NotImplementedError
