from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
import sys

import config
from ..logging import LOGGER


class DAXX(Client):
    def __init__(self, name="ZoyuXmusicRobot"):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name=name,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode="html",
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = self.me.first_name + (" " + self.me.last_name if self.me.last_name else "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure the bot is added as admin."
            )
            sys.exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel. Reason: {type(ex).__name__}"
            )
            sys.exit(1)

        member = await self.get_chat_member(config.LOGGER_ID, self.id)
        if member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            sys.exit(1)

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()