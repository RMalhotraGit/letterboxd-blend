"""Command-line interface."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="letterboxd-blend",
        description="Recommend movies two Letterboxd users would both like.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("export_a", help="Path to the first person's unzipped export")
    parser.add_argument("export_b", help="Path to the second person's unzipped export")
    parser.add_argument("-n", "--top", type=int, default=10, help="Number of recommendations")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(f"TODO: blend {args.export_a} + {args.export_b} (top {args.top})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
