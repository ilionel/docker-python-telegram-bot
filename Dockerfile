FROM python:3.14-alpine AS bot

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# The bot token is provided at RUNTIME only (never baked into the image).
RUN pip install --upgrade pip

RUN adduser -D telegram-bot
USER telegram-bot
WORKDIR /home/telegram-bot
ENV PATH="/home/telegram-bot/.local/bin:${PATH}"

COPY --chown=telegram-bot:telegram-bot requirements.txt bot.py /home/telegram-bot/

RUN pip install --user -r requirements.txt

CMD ["python3", "bot.py"]
