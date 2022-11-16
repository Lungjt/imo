import telebot
from decouple import config

api_id = config ('api_id')
api_hash = config ('api_hash')
BOT_TOKEN = config('TOKEN_BOT')

bot = telebot.Telebot(BOT_TOKEN)



@bot.message_handler(commanos=["start", "help"])
def welcome(message):
    bot.send_message(message.chat.id, "hello everyone")
    
    bot.polling()