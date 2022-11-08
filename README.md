# docker-python-telegram-bot
### Docker image and CI pipline of https://github.com/python-telegram-bot/python-telegram-bot

1. Create your bot using https://telegram.me/BotFather
2. Copy your token on `.env` file : `TELEGRAM_TOKEN=xxxxxxxx`
3. Build and run docker image : `docker-compose up --build`

### Now if you start discution with your bot:

1. In Telegram, go to your bot and type /hello.
2. The bot should answer `Hello <your first name>`.

Write your own code (to personalize the bot). You should add it into the `bot.py` file.
