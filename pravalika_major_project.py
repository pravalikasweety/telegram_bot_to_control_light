!pip install python-telegram-bot
!pip install adafruit-io
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import Update
import requests
from Adafruit_IO import Client,Data
import os

def turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Led turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')
  send_value(0)
def turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Led turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://img.icons8.com/plasticine/2x/light-on.png')
  send_value(1)

def send_value(value):
  feed = aio.feeds('light')
  aio.send_data(feed.key,value)

def input_message(update, context):
  text=update.message.text
  if text == 'turn on':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Led turned on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://img.icons8.com/plasticine/2x/light-on.png')
  elif text == 'turn off':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Led turned off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')

def start(update,context):
  start_message='''
/turnoff or 'turn off':To turn of the led ,sends value=0 in feed
/turnon or 'turn on'  :To turn on the led ,sends value=1 in feed
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
  
  ADAFRUIT_IO_USERNAME = os.getenv('pravalika_sweety')  #username declared
ADAFRUIT_IO_KEY = os.getenv('aio_WcAk72SdCo282f4dE8XopX8C6ToG') #io key declared
TOKEN = os.getenv('1382715006:AAHkAgkK6FYTwR_mzJhGrKCwJeRplWyArIk') #token declared

aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
updater=Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoff',turnoff))
dispatcher.add_handler(CommandHandler('turnon',turnon))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()

