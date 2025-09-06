from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHINxSANATANIxMUSIC import app
from config import BOT_USERNAME
from SACHINxSANATANIxMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
〄 ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ sᴀᴄʜɪɴ sᴀɴᴀᴛᴀɴɪ ʀᴇᴘᴏs 〄
 
࿃ ᴍᴇʀᴀ ʟᴀɴᴅ ʟᴇ ʟᴇ
 
࿃ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ ʀᴀɴᴅɪ ᴋᴇ
 
࿃ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ
 
"""




@app.on_message(filters.command("ISrepo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＡＤＤ ＭＥ ＢＡＢＹ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/SANATANI_IS_HERE"),
          InlineKeyboardButton("ＳＡＣＨＩＮ", url="https://t.me/V_VIP_OWNER"),
          ],
               [
                InlineKeyboardButton("ＳＡＮＡＴＡＮＩ ＮＥＴＷＯＲＫ", url=f"https://t.me/SANATANI_IS_HERE"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/HIMANSHI_MUSIC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/9131bdd30ab9c76349f25.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
        has_spoiler=True
    )
