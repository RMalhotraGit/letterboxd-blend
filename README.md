# letterboxd-blend

Takes two people's Letterboxd data (watched films, ratings, diary entries) and
recommends movies they would both like.

## Getting started

Export your data from Letterboxd (Settings → Data → Export your data), unzip it,
then:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

letterboxd-blend path/to/alice_export path/to/bob_export -n 10
```

## Development

```bash
pytest          # run tests
ruff check .    # lint
mypy            # type-check
```

## Layout

```
src/letterboxd_blend/
  models.py   Movie, DiaryEntry, Profile, Recommendation
  loader.py   Parse a Letterboxd export into a Profile
  blend.py    The blend algorithm
  cli.py      Command-line entry point
tests/
```

## Roadmap

- [ ] Parse `watched.csv`, `ratings.csv`, `diary.csv`
- [ ] Taste-similarity score between two profiles
- [ ] Rating prediction per candidate movie
- [ ] Combine both people's predictions into a blended ranking
- [ ] Source of candidate movies (catalog)
