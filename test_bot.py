from unittest.mock import AsyncMock, MagicMock

import bot


async def test_hello_replies_with_the_user_first_name():
    update = MagicMock()
    update.effective_user.first_name = "Lionel"
    update.message.reply_text = AsyncMock()

    await bot.hello(update, MagicMock())

    update.message.reply_text.assert_awaited_once_with("Hello Lionel")
