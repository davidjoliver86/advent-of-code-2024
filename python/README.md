# Advent of Code 2024 in Python
Experimenting with Rust-based tooling (e.g. `ruff`, `uv`) this time around.

## Ruff linter rules
Ruff linter rules are taken from the recommended ruleset in the [docs](https://docs.astral.sh/ruff/linter/#__tabbed_2_1):
```
[tool.ruff.lint]
select = [
    # pycodestyle
    "E",
    # Pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
]
```

## Formatting
Formatting is done with `ruff format`, and replacing `isort` is `ruff check --select I --fix`.