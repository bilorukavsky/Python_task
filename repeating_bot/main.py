import logging
import os

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    ContextTypes
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(text = "Add a photo", callback_data='1')],
        [InlineKeyboardButton(text = "GitHub", url = 'https://github.com/bilorukavsky/python_task')],
        [InlineKeyboardButton(text = "Quote", callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Hi!')
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

    
def photo(update: Update, context: CallbackContext) -> None:
    photo_file = update.message.photo.get_file()
    photo_file.download('user_photo.jpg')
    logger.info('user_photo.jpg')
    update.message.reply_text('Add to photo')


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if (query.data== '1'):
        photo(query,context)
    elif(query.data == '2'):
       query.edit_message_text("Quote")
    query.answer()


def main() -> None:
    updater = Updater(os.environ["TOKEN"])

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
