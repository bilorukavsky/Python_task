import logging
import os
import requests

from telegram import (
    Update,
    ForceReply,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup
)

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes
)

from pprint import pprint

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def _get_unix_timestamp() -> int:
    """Returns unix timestamp."""

    import time 
    from datetime import datetime 

    return int(time.mktime(datetime.now().timetuple()))


def start(update: Update, context: CallbackContext) -> None:
    #keyboard = [
    #    [InlineKeyboardButton(text = "Add a photo", callback_data='1')],
    #    [InlineKeyboardButton(text = "GitHub", url = 'https://github.com/bilorukavsky/python_task')],
    #    [InlineKeyboardButton(text = "Quote", callback_data='2')]
    #]
    #reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Hi!')
    update.message.reply_text('Please choose:', reply_markup=markup())


def markup() -> list:
    keyboard = [
        [InlineKeyboardButton(text="Add a photo", callback_data='1')],
        [InlineKeyboardButton(text="GitHub", url='https://github.com/bilorukavsky/python_task')],
        [InlineKeyboardButton(text="Quote", callback_data='2')]
    ]
    return InlineKeyboardMarkup(keyboard)


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

    
def photo(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user

    photo_file = update.message.photo[-1].get_file()
    photo_file.download(f'photos/{user.id}_{_get_unix_timestamp()}.jpg')

    logger.info(f"{user.first_name} {user.last_name} @{user.username} {user.id} uploaded photo")
    update.message.reply_text('Photo added')
    update.message.reply_text('Please choose:', reply_markup=markup())

    
def quote() -> dict:
    with requests.get('https://zenquotes.io/api/random') as r:
        if r.status_code == 200:
            response = r.json()
            return response
        else:
            r.raise_for_status()
           
        
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    if query.data == '1':
        message = query.edit_message_text("Upload a photo:")

    elif query.data == '2':
        response = quote()
        query.edit_message_text(f"Quote: {response[0]['q']}")
        message = query.message.reply_text(f"Author: {response[0]['a']}")
        context.bot.send_message(message.chat_id, 'Please choose:', reply_markup=markup())
    
    query.answer()


def main() -> None:
    updater = Updater(os.environ["TOKEN"])

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CallbackQueryHandler(button))

    dispatcher.add_handler(MessageHandler(Filters.photo, photo))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
