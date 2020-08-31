 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import translation.py

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton


from helper_funcs.chat_base import TRChatBase


@pyrogram.Client.on_callback_query()
async def cb_handler(bot, update):

    if "get_start" in update.data:
        await update.message.delete()
        await send_start(bot, update.message)     
    elif "get_help" in update.data:
        await update.message.delete()
        await help_user(bot, update.message)
    elif "close" in update.data:
        await update.message.delete()
    elif "get_about" in update.data:
        await update.message.delete()
        await about(bot, update.message)


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=translation.HELP_USER,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/TroJanzHEX")],
                                           [InlineKeyboardButton(text="🔙 BACK", callback_data="get_start"), InlineKeyboardButton(text="💢 ABOUT", callback_data="get_about"), InlineKeyboardButton(text="✖️ CLOSE", callback_data="close")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def send_start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://t.me/TroJanzHEX"), InlineKeyboardButton(text="⭕️ SUPPORT ⭕️", url="https://t.me/contactHEXbot")],
                                                    [InlineKeyboardButton(text="🆘 HELP 🆘", callback_data="get_help"), InlineKeyboardButton(text="♐️ SHARE ♐️", url="tg://msg?text=Hai%20Friend%20%E2%9D%A4%EF%B8%8F%2C%0AToday%20i%20just%20found%20out%20an%20intresting%20and%20Powerful%20%2A%2ARename%20Bot%2A%2A%20for%20Free%F0%9F%A5%B0.%20%0A%2A%2ABot%20Link%20%3A%2A%2A%20%40TroJanzRenamer%20%F0%9F%94%A5")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )



@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=translation.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🔙 BACK 🔙", callback_data="get_help"), InlineKeyboardButton(text="✖️ CLOSE ✖️", callback_data="close")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    )  
    
