import telebot
import requests 
from telebot import *
token = "5547000805:AAFhuL3WuuDHxE8cyhtKafcinYb1EWapB8g"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.first_name
    key = types.InlineKeyboardMarkup()
    bot1 = types.InlineKeyboardButton('[=] 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 [1]' ,url ='https://t.me/oorog')
    bot2 = types.InlineKeyboardButton('[=] 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 [2]' ,url ='https://t.me/Oporv')
    bot3 = types.InlineKeyboardButton(text=f'[=] 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 {use} ' ,callback_data='k2')
    key.add(bot3)
    key.add(bot1,bot2)
    p1ng = "https://i.postimg.cc/66mYfP2H/image.jpg"
    bot.send_photo(message.chat.id,p1ng,reply_markup=key)
    bot.send_message(message.chat.id, text = f"<strong> [=] 𝚂𝙴𝙽𝙳 𝙽𝙰𝙼𝙴  </strong>",parse_mode="html")
    @bot.message_handler(func=lambda message: True)
    def start(message):
        url = (f"https://timoa.ml/Novels.php?search={message.text}")
        sd = requests.get(url).json()
        a = sd['results']['url']
        e = sd['results']['title']
        if a == 'https://www.kotobati.com/' :
            bot.send_message(message.chat.id, text = f"<strong> [=] 𝙱𝙰𝙳 𝙽𝙰𝙼𝙴  </strong>",parse_mode="html")
            bot.send_message(message.chat.id, text = f"<strong> [=] 𝚂𝙴𝙽𝙳 𝙽𝙰𝙼𝙴  </strong>",parse_mode="html")
        else : 
            key1 = types.InlineKeyboardMarkup()
            bot11 = types.InlineKeyboardButton('[=] 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 [=]' ,url ='https://t.me/IIlAndylII')
            key1.add(bot11)
            bot.send_document(message.chat.id,a,caption=f'<strong> {e} </strong>',parse_mode="html",reply_markup=key1)
            bot.send_message(message.chat.id, text = f"<strong> [=] 𝚂𝙴𝙽𝙳 𝙽𝙰𝙼𝙴  </strong>",parse_mode="html")


bot.polling(True)	 
