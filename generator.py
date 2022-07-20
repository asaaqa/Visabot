from telebot import *
import telebot
token = "5547000805:AAFhuL3WuuDHxE8cyhtKafcinYb1EWapB8g"
bot = telebot.TeleBot(token)
def start(message):
    use =  message.from_user.username
    key =  types.InlineKeyboardMarkup()
    bot1 =  types.InlineKeyboardButton('• قناة المطور 1 •' ,url ='https://t.me/oyurl')
    bot2 = types.InlineKeyboardButton('• قناة المطور 2 •' ,url ='https://t.me/Oporv')
    bot3 =  types.InlineKeyboardButton('• لبدء الاستخدام قم بارسال النص؟ •' ,callback_data='d1')
    key.add(bot2,bot1)
    key.add(bot3)
    bot.send_photo(message.chat.id,'https://pin.it/4RuPdeO',f"""<strong>
• اهلا بك عزيزي @{use} .

• في بوت الدفتر الالكتروني  .

• الدفتر فقط بالغه الانكليزيه  .
</strong>""",parse_mode="html",reply_to_message_id=message.message_id,reply_markup=key)

@bot.message_handler(func=lambda message: True)
def start(message):
    key =  types.InlineKeyboardMarkup()
    bot6 =  types.InlineKeyboardButton('• للاستخدام مرة اخرى قم بارسال النص •' ,callback_data ='d2')
    bot7 =  types.InlineKeyboardButton('• لمراسله مطور البوت اضغط هنا •' ,url ='https://t.me/IIlAndylII')
    key.add(bot7)
    key.add(bot6)
    url = (f"http://apis.xditya.me/write?text={message.text}")
    bot.send_photo(message.chat.id,url,reply_markup=key)


bot.polling(True)
