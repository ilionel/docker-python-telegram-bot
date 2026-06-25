import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply to /hello with a greeting."""
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


def main() -> None:
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise SystemExit("TELEGRAM_TOKEN environment variable is not set")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("hello", hello))

    # Blocking; runs until the process receives SIGINT/SIGTERM/SIGABRT.
    application.run_polling()


if __name__ == "__main__":
    main()
