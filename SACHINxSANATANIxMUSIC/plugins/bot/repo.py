from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHINxSANATANIxMUSIC import app
from config import BOT_USERNAME
from SACHINxSANATANIxMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
<b>:⧽ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ˹ᴧᴧʀᴜᴍɪ ꭙ ʙᴏᴛѕ˼ ʀᴇᴘᴏs</b> 
 
<b>:⧽ ʀᴇᴘᴏ ᴛᴏ ɴʜɪ ᴍɪʟᴇɢᴧ ʙʜᴧɪ ʏʜᴧ</b>
 
<b>:⧽ ᴧɢᴧʀ ʀᴇᴘᴏ ᴄʜᴧʜɪʏᴇ ᴛᴏ ʙʜᴧɪ ʀᴇᴘᴏ ᴘᴧɪᴅ ᴍɪʟ ᴊᴀʏᴇɢᴧ</b>
 
<b>:⧽ ᴄᴏɴᴛᴧᴄᴛ :    - к ᴧ ʀ м ᴧ › ᴏᴘ ⇢</b>

<b>:⧽ ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ</b>
 
"""




@app.on_message(filters.command("repo") & filters.private)
async def repo_cmd(_, msg):
    # Sirf /repo allow karna hai
    if msg.text.strip() != "/repo":
        return
    buttons = [
        [ 
          InlineKeyboardButton("⊚ ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ⊚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇ", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat"),
          ],
               [
                InlineKeyboardButton("ʙᴏᴛꜱ ᴏᴡɴᴇʀ", url=f"https://t.me/Swagger_Soul"),
],
[
InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴧʟ ᴍυꜱɪᴄ ʙᴏᴛ", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://ibb.co/xtbmK9dy",
        caption=start_txt,
        reply_markup=reply_markup,
        has_spoiler=True,
        parse_mode="html"
 
    )
