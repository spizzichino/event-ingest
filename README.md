# event-ingest

An HTTP service that accepts readings from devices, one at a time or in batches, stores them
in PostgreSQL, and serves them back by device and time range. Ingestion is idempotent, so
devices can safely retry after a timeout.

> Work in progress. Built step by step; see the commit history.

## Run locally

```sh
uv sync
uv run pytest
uv run fastapi dev src/event_ingest/main.py   # once main.py exists
```

## Checks

```sh
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
```

## Design decisions

Short records of the main decisions are in [docs/adr](docs/adr).

## Licence

MIT
