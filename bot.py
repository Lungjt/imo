import telebot
from decouple import config

BOT_TOKEN = config('TOKEN_BOT')

bot = telebot.Telebot(BOT_TOKEN)



@bot.message_handler(commanos=["start", "help"])
def welcome(message):
    bot.send_message(message.chat.id, "hello everyone")
    
    bot.polling()