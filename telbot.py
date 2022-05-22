import telebot
from telebot import types
import random

bot = telebot.TeleBot("5197848675:AAGosvoLHWrpC8U1ctPEmbT7aCTvAC_h5IQ")
#bot token 
#bot start command 
@bot.message_handler(commands=['start'])
def start(message):
   mess = f'Привет, {message.from_user.first_name} Напиши /help'
   bot.send_message(message.chat.id, mess)
#bot start command end

#password randomizer
small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
use_for = small + big + numbers + symbols 
pass_length = 10

password = "".join(random.sample(use_for, pass_length))
#password randomizer end


#help command 
#Buttons
@bot.message_handler(commands=['help'])
def buttons(message):
   markup = types.ReplyKeyboardMarkup() 
   website = types.KeyboardButton('/website')  #create button with /website command
   instagram = types.KeyboardButton('/instagram') #create button with /instagram command
   passgener = types.KeyboardButton('/passwordgenerator') ##create button with /passwordgenerator command
   markup.add(website, instagram, passgener) #adding website, instagram, passgener markups
   bot.send_message(message.chat.id, 'Выберите', reply_markup=markup) #bot sending message
#Buttons endw
#help command end

#command /website   
@bot.message_handler(commands=['website'])
def website(message):
   markup = types.InlineKeyboardMarkup()
   markup.add(types.InlineKeyboardButton('Посетите мой веб-сайт', url = "http://freez.zzz.com.ua")) #creating Inlinebutton with url  
   bot.send_message(message.chat.id, "Перейти на сайт", reply_markup=markup) #bot sending message
#command /website end

#command /instagram
@bot.message_handler(commands=['instagram'])
def instagram(message):
   markup = types.InlineKeyboardMarkup()
   markup.add(types.InlineKeyboardButton('Посетить мой инстаграм', url = "https://www.instagram.com/aidynissa/")) #creating Inlinebutton with url
   bot.send_message(message.chat.id, "Перейти в инстаграм", reply_markup=markup) #bot sending message
#command /instagram end 

#command passwordgenerator
@bot.message_handler(commands=['passwordgenerator'])
def passgen(message):
   mess = f"Твой Пароль: " + password #using password from 24 line
   bot.send_message(message.chat.id, mess) #bot sending message
#command passwordgenerator end

#handler with text commands
@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello': 
      bot.send_message(message.chat.id, 'И тебе привет',) 
    elif message.text == 'ID':
      bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}') #sending User ID to chat
#handler with text commands  

#none stoper
bot.polling(none_stop=True)
#none stoper end
