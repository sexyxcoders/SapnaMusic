from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Import your bot app and username from your main bot file
from SACHINxSANATANIxMUSIC import app
from config import BOT_USERNAME 

start_txt = """
**:⧽ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ˹ᴧᴧʀᴜᴍɪ ꭙ ʙᴏᴛѕ˼ ʀᴇᴘᴏs**

**:⧽ ʀᴇᴘᴏ ᴛᴏ ɴʜɪ ᴍɪʟᴇɢᴧ ʙʜᴧɪ ʏʜᴧ**

**:⧽ ᴧɢᴧʀ ʀᴇᴘᴏ ᴄʜᴧʜɪʏᴇ ᴛᴏ ʙʜᴧɪ ʀᴇᴘᴏ ᴘᴧɪᴅ ᴍɪʟ ᴊᴀʏᴇɢᴧ**

**:⧽ ᴄᴏɴᴛᴧᴄᴛ : - к ᴧ ʀ м ᴧ › ᴏᴘ ⇢**

**:⧽ ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ**
"""

@app.on_message(filters.command("repo") & (filters.private | filters.group))
async def repo_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("⊚ ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ⊚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇ", url="https://t.me/AarumiBots"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat")
        ],
        [InlineKeyboardButton("ʙᴏᴛꜱ ᴏᴡɴᴇʀ", url="https://t.me/Swagger_Soul")],
        [InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴛʟ ᴍυꜱɪᴄ ʙᴏᴛ", url="https://t.me/AarumiSongBot")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://telegra.ph/file/9131bdd30ab9c76349f25.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
        parse_mode="HTML",  
        disable_notification=True,
        has_spoiler=True
    )
    
