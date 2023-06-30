from . import *
import requests as r
import re
from telethon import events
read=r.get("https://gist.githubusercontent.com/itz-king/1b98aa6ec756058144d66e306fc557dc/raw/pokemon.txt").text

@bot.on(events.NewMessage(chats=SPECIAL_GUESS))
async def guessing(event):
    if event.sender_id == 572621020:
        if not event.photo :
            if 'Hint' in event.raw_text:
                string=event.raw_text
                string=string[8:]
                toreplace = {'_': '.',' ': ''}
                for key, value in toreplace.items():
                    string = string.replace(key, value)
                patt = re.compile(string)
                matches = patt.finditer(read)
                for match in matches:
                    await event.client.send_message(event.chat_id,f"{match[0]}")

@bot.on(events.NewMessage(chats=SPECIAL_GUESS))
async def gues(event):
  if event.sender_id == 572621020:
        if not event.photo :
            if '+5' in event.raw_text:
                await event.client.send_message(event.chat_id,"/guess")
