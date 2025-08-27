from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHINxSANATANIxMUSIC import app
from config import BOT_USERNAME

start_txt = """
**:⧽ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ˹ᴧᴧʀᴜᴍɪ ꭙ ʙᴏᴛѕ˼ ʀᴇᴘᴏs**

**:⧽ ʀᴇᴘᴏ ᴛᴏ ɴʜɪ ᴍɪʟᴇɢᴧ ʙʜᴧɪ ʏʜᴧ**

**:⧽ ᴧɢᴧʀ ʀᴇᴘᴏ ᴄʜᴧʜɪʏᴇ ᴛᴏ ʙʜᴧɪ ʀᴇᴘᴏ ᴘᴧɪᴅ ᴍɪʟ ᴊᴀʏᴇɢᴧ**

**:⧽ ᴄᴏɴᴛᴧᴄᴛ :    - к ᴧ ʀ м ᴧ › ᴏᴘ ⇢**

**:⧽ ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ**
"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [InlineKeyboardButton("⊚ ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ⊚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇ", url="https://t.me/AarumiBots"),
         InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat")],
        [InlineKeyboardButton("ʙᴏᴛꜱ ᴏᴡɴᴇʀ", url="https://t.me/Swagger_Soul")],
        [InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴧʟ ᴍυꜱɪᴄ ʙᴏᴛ", url="https://t.me/AarumiSongBot")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://telegra.ph/file/9131bdd30ab9c76349f25.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
        parse_mode="markdown",
        has_spoiler=True
    )
