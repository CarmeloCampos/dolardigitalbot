import logging

from telegram.ext import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def listener(update, context):
    id = update.message.chat_id
    mensaje = update.message.text
    print("ID: " + str(id) + " Mensaje: " + mensaje)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def test(update, context):

    update.message.reply_photo('https://tierravivaplanet.com/img/8feb.png', caption=update.message.chat_id)


def main():
    updater = Updater(
        "", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("test", test))

    dp.add_handler(MessageHandler(Filters.text, listener))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
