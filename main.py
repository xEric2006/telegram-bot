import os
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Lấy token từ biến môi trường

def start(update, context):
    update.message.reply_text("🤖 Bot hoạt động rồi nè!")

updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
