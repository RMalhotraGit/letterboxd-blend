"""Load a Letterboxd data export into a Profile.

A Letterboxd export (Settings -> Data -> Export your data) is a zip containing,
among others, ``watched.csv``, ``ratings.csv`` and ``diary.csv``.
"""

from __future__ import annotations

from pathlib import Path

from .models import Profile


def load_profile(export_dir: str | Path, username: str) -> Profile:
    """Build a Profile from an unzipped Letterboxd export directory.

    TODO: parse watched.csv, ratings.csv and diary.csv.
    """
    export_dir = Path(export_dir)
    if not export_dir.is_dir():
        raise FileNotFoundError(f"Export directory not found: {export_dir}")
    return Profile(username=username)
