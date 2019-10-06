import logging
import os
import random
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def start_handler(bot, update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("Soy mesquina jijiji")
    
def abraso_handler(bot, update):
    logger.info("User {} asked for abraso".format(update.effective_user["id"]))
    update.message.reply_text("Abrasooooo")

def handle_message(bot, update):
    text = update.message.text
    if "ABRASO" in str.upper():
        update.message.reply_text("Si quieres que haga algo tienes que usar un comando")
    else:
        mimimiString = ""
        mimimiString = text.replace("a", "i").replace("e", "i").replace("o", "i").replace("u", "i")
        mimimiString = mimimiString.replace("A", "I").replace("E", "I").replace("O", "I").replace("U", "I")
        mimimiString = mimimiString.replace("á", "í").replace("é", "í").replace("ó", "í").replace("ú", "í")
        mimimiString = mimimiString.replace("Á", "Í").replace("É", "Í").replace("Ó", "Í").replace("Ú", "Í")
        
        mimimiList = list(mimimiString)
        for i in range (0, mimimiList):
            if (mimimiList[i] == "u" or mimimiList[i] == "U" or mimimiList[i] == "ú" or mimimiList[i] == "Ú"):
                if (mimimiList[i-1] == "g" or mimimiList[i-1] == "G" or mimimiList[i-1] == "q" or mimimiList[i-1] == "Q"):
                    continue
                elif (mimimiList[i] == "u"):
                    mimimiList[i] = "i"
                elif (mimimiList[i] == "ú"):
                    mimimiList[i] = "í"
                elif (mimimiList[i] == "U"):
                    mimimiList[i] = "I"
                elif (mimimiList[i] == "Ú"):
                    mimimiList[i] = "Í"
        
        mimimiStringResult = "".join(mimimiList)
        update.message.reply_text(mimimiStringResult)

if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("abraso", abraso_handler))
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handle_message))

    run(updater)