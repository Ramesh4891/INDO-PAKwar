from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Import from config
from config import BOT_TOKEN

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to INDO-PAK War Bot!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
