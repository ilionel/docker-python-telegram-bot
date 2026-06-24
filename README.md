# docker-python-telegram-bot

[![CI](https://github.com/ilionel/docker-python-telegram-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/ilionel/docker-python-telegram-bot/actions/workflows/ci.yml)

A minimal, container-ready [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
(v21, async) starter. Bring your token, write your handlers in [`bot.py`](bot.py).

## Quick start

1. Create a bot and copy its token from [@BotFather](https://telegram.me/BotFather).
2. Put the token in a `.env` file next to `docker-compose.yml`:

   ```dotenv
   TELEGRAM_TOKEN=123456:your-token
   ```

3. Build & run:

   ```sh
   docker compose up --build
   ```

The token is read at **runtime only** (never baked into the image), and `.env` is git-ignored.

## Try it

In Telegram, open your bot and send `/hello` — it replies `Hello <your first name>`.

## Develop

Add your handlers in [`bot.py`](bot.py) (async, `python-telegram-bot` v21 API):

```sh
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
TELEGRAM_TOKEN=… python bot.py
```

## Tooling

- **Lint/format**: [`ruff`](https://docs.astral.sh/ruff/) — `ruff check` & `ruff format --check`.
- **Dockerfile lint**: [`hadolint`](https://github.com/hadolint/hadolint).
- Both run in CI ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)).
- Pinned base image (`python:3.12-alpine`) and dependency (`python-telegram-bot[all]~=21.0`).
