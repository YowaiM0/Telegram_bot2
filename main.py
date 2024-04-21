import random 
import telebot
from bot_token import TOKEN 

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(func=lambda x: 'рандом' in x.text
)
def send_random (message):
    bot.send_message(message.chat.id, f'Случайное число: {random.randint(0, 100)}')

@bot.message_handler(content_types=['text']
                     
)
def echo(message):
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot.infinity_polling()  
   
