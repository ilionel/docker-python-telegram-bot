FROM alpine AS bot

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# Env vars
ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

RUN apk add --no-cache python3 py3-pip
RUN pip install --upgrade pip

RUN adduser -D telegram-bot
USER telegram-bot
WORKDIR /home/telegram-bot

COPY --chown=telegram-bot:telegram-bot requirements.txt bot.py /home/telegram-bot/

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
