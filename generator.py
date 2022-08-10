import asyncio
import os
import re
import requests
import wget
import yt_dlp


from pyrogram.errors import FloodWait
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
#-----------[ Colors ]-----------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
r = "1234567890"
#------------------------------[Start CoDe]------------------------------
token = "5597319843:AAE0aEjolfWE9fbiWYl_fUj3Tb7QfGRO7LE"
import webbrowser  
import requests
import random
import telebot
import os
from telebot import types
from uuid import uuid4
import webbrowser
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def Start(message):
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 A = types.InlineKeyboardMarkup(row_width = 2)
 B = types.InlineKeyboardButton("- channel  ", url = "t.me/oyurl")
 C = types.InlineKeyboardButton("- Developer ", url = "t.me/IIlAndylII")
 A.add(B,C)
 bot.send_message(message.chat.id, text=  """
*- 👋اهلا عزيزي*  [{}](tg://settings/)       
*- فــي بــⲃ๐тــوت تحميل صوت يوتيوب     
*- فـقـط قـ۾ بـاࢪسـال اسـمـك ❤️‍🔥*      
*- أيدك :* [{}](tg://settings/)            
*- يوزرك :* @{}       """.format(Name,ID,User) , parse_mode = "markdown", reply_markup = A)



Deo = Client(
    "Bot",
    api_id =  14359685,
 api_hash = "7a1d44bbc22a573f71ea1e4030065dcb",
 bot_token = "5597319843:AAE0aEjolfWE9fbiWYl_fUj3Tb7QfGRO7LE"
)

       
flex = {}
chat_watcher_group = 3

                       
ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}        

@bot.on_message(filters.command("بحث", [".", ""]))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**🔄 Searching.... **")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("**⚠️ No results were found. Make sure you typed the information correctly**")
        print(str(e))
        return
    m.edit("**📥 Downloading ..**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**📤 Uploading ..**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)           
        
        
bot.polling(True)
