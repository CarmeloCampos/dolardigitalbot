import logging

from telegram.ext import *
from datetime import datetime


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def echo_user(id, mensaje):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%d/%b/%Y %H:%M:%S)")
    print("ID: " + str(id) + " Mensaje: " + mensaje + "  Hora: " + timestampStr)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def price(update, context):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%d_%b_%Y_%H)")
    update.message.reply_photo('https://damianicash.pro/p2p/imagen_i.png' +
                               timestampStr, caption="Precio de Dolar Today (COMPARACIONES)")
    echo_user(update.message.chat_id, update.message.text)


def dolartoday(update, context):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%d_%b_%Y_%H)")
    url = 'https://dxj1e0bbbefdtsyig.woldrssl.net/custom/rate2.jpg?timestampStr='+timestampStr
    update.message.reply_photo(
        url, caption="Precio tomado de: https://dolartoday.com/")
    echo_user(update.message.chat_id, update.message.text)


def start(update, context):
    update.message.reply_text(parse_mode="HTML", text='<b>BOT CONSULTA DEL DOLAR</b>\nConsulta el precio del dolar en tiempo real!\n<b>Creado por @CamposCarmelo</b>\n\nComandos disponibles: \n/price : Muestra el precio de DOLAR DIGITAL\n/start : Muestra este mensaje\n/dolartoday : Muestra el precio de DolarToday.com\n\n(ESTOS PRECIOS SE ACTUALIZAN CADA HORA).\n\n/price_hd : Envia el precio de DOLARDIGITAL como documento (En tiempo real).')
    echo_user(update.message.chat_id, update.message.text)


def price_hd(update, context):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("(%d_%b_%Y__%H_%M)")
    update.message.reply_document(
        'https://damianicash.pro/p2p/imagen_i.png'+timestampStr)
    echo_user(update.message.chat_id, update.message.text)


def main():
    updater = Updater(
        "", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", price))
    dp.add_handler(CommandHandler("dolartoday", dolartoday))
    dp.add_handler(CommandHandler("price_hd", price_hd))

    dp.add_handler(MessageHandler(Filters.text, start))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
