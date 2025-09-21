from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus

import config
from ..logging import LOGGER


# 🔴 Hardcode your log group/channel ID here
LOG_CHAT = -1003072931688   # replace with your real log group ID


class DAXX(Client):
    def init(self):
        LOGGER(name).info("Starting Bot...")
        super().init(
            name="ZoyuXmusicRobot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode="html",   # added to handle HTML formatting
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()   # ✅ fetch bot info safely
        self.id = self.me.id
        self.name = self.me.first_name + (" " + self.me.last_name if self.me.last_name else "")
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
            LOGGER(name).error(
                "Bot has failed to access the log group/channel. "
                "Make sure you added the bot to the log group/channel."
            )
            import sys; sys.exit(1)
        except Exception as ex:
            LOGGER(name).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).name}."
            )
            import sys; sys.exit(1)

        a = await self.get_chat_member(LOG_CHAT, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(name).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            import sys; sys.exit(1)

        LOGGER(name).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
