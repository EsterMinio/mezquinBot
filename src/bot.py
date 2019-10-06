# This file contains the source code of MezquinBot a friendly and polite Telegram Bot.

from telegram.ext import Updater, CommandHandler
from config.auth import token

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('MezquinBot')


def start(bot, update):
    logger.info('He recibido un comando start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Soy MezquinBot, voy a ser mezquina contigo."
    )


if __name__ == '__main__':

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
