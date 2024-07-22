#credit @codeflix_bots (telegram)
# yt : https://www.youtube.com/@ultroidofficial

"""Get id of the replied user
Syntax: /id"""

from pyrogram import filters, enums
from pyrogram.types import Message

from bot import Bot  # Assuming this imports your bot instance


@Bot.on_message(filters.command("id") & filters.private)
async def show_user_id(client: object, message: Message) -> None:
    """Responds to the `/id` command in private chats, returning the ID of the replied user (if any) or the user who sent the message."""

    if message.reply_to_message:  # Check if responding to a message
        replied_user_id = message.reply_to_message.from_user.id
        await message.reply_text(
            f"**Replied user ID:** `{replied_user_id}`", quote=True
        )
    else:
        user_id = message.from_user.id
        await message.reply_text(
            f"**Your user ID:** `{user_id}`", quote=True
        )

