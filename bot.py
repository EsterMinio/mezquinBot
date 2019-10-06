# bot.py

from telegram.ext import Updater, CommandHandler
from flask import Flask, request
import requests  
import os
import logging
# Add your telegram token as environment variable
#BOT_URL = f'https://api.telegram.org/bot920184271:AAGf49s0Ju_QYTBPA_HTYOqjSOniAe1qyLg/'


app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('AchicaynaBot')


#@app.route('/', methods=['POST'])
#def main():  
 #   logger.info('Hola')

  #  data = request.json

   # print(data)  # Comment to hide what Telegram is sending you
    #chat_id = data['message']['chat']['id']
    #message = data['message']['text']

    #json_data = {
    #    "chat_id": chat_id,
    #    "text": message,
    #}

    #message_url = BOT_URL + 'sendMessage'
    #requests.post(message_url, json=json_data)

    #return ''
    

def start(bot, update):
    logger.info('He recibido un comando start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Soy Mesquina jijiji."
    )



if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
    updater = Updater(token='920184271:AAGf49s0Ju_QYTBPA_HTYOqjSOniAe1qyLg', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

