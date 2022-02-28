import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/70167c6712b97ebcb55ec.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Hi its kita on this side** \n\n"
  YUMEKO += "×**I'm playing great!** \n\n"
  YUMEKO += "×**My Owners : [VOID](https://t.me/voidxtoxic) , [IRIS](https://t.me/slime_vidda)** \n\n"
  YUMEKO += f"×**Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"×**Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**yeh yeh thanks for adding baka!**"
  BUTTON = [[Button.url("•Support•", "https://t.me/horimiya_family"), Button.url("•Network•", "https://t.me/void_network")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  YUMEKO = "✅ **nice i feel refreshing!**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("•creator•", "https://t.me/voidxtoxic")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)
