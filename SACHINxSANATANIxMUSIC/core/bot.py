from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus

import config
from ..logging import LOGGER


# 🔴 Hardcode your log group/channel ID here
LOG_CHAT = -1003072931688  # replace with your real log group ID


class DAXX(Client):
    def __init__(self):
        LOGGER("DAXX").info("Initializing Bot Client...")
        super().__init__(
            name="ZoyuXmusicRobot",   # session name (required)
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode="html",  # allow HTML formatting
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = self.me.first_name + (
            " " + self.me.last_name if self.me.last_name else ""
        )
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=LOG_CHAT,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER("DAXX").error(
                "Bot failed to access the log group/channel. "
                "Make sure you added the bot to the log group/channel."
            )
            import sys
            sys.exit(1)
        except Exception as ex:
            LOGGER("DAXX").error(
                f"Bot failed to access the log group/channel.\nReason: {type(ex).__name__}."
            )
            import sys
            sys.exit(1)

        # ✅ Check if bot is admin in log group
        a = await self.get_chat_member(LOG_CHAT, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER("DAXX").error(
                "Please promote your bot as an admin in your log group/channel."
            )
            import sys
            sys.exit(1)

        LOGGER("DAXX").info(f"Music Bot Started as {self.name}")

    async def stop(self):
        LOGGER("DAXX").info("Stopping Bot...")
        await super().stop()
