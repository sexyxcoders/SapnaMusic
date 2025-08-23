from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHINxSANATANIxMUSIC import app
from config import BOT_USERNAME
from SACHINxSANATANIxMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - sᴀᴄʜɪɴ sᴀɴᴀᴛᴀɴɪ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ᴘʀɪɴᴄᴇ ʀᴀᴊᴘᴜᴛ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @Swagger_Soul
├┤~ @AarumiBots
├┤~ @AarumiChat
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @Swagger_Soul
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton(" 𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 ", url=f"https://t.me/Swagger_Soul")
        ],
        [
          InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇ", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat"),
          ],
               [
                InlineKeyboardButton("ʙᴏᴛ ʟɪsᴛ", url=f"https://t.me/AarumiBots/4"),
],
[
InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴧʟ ᴍυꜱɪᴄ ʙᴏᴛ", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/94f5088fdc7a0450bfa0a.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
