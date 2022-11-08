import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def main():
    # We create an Updater instance with our Telegram token.
    updater = Updater(os.environ.get("TELEGRAM_TOKEN"))

    # We register our command handlers.
    updater.dispatcher.add_handler(CommandHandler("hello", hello))

    # Let's start the bot!
    # Calling this method is non-blocking.
    updater.start_polling()

    # Run the bot until you press Ctrl-C.
    # Or until the process receives SIGINT, SIGTERM or SIGABRT.
    updater.idle()


if __name__ == "__main__":
    main()
