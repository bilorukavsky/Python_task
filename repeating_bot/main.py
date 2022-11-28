import logging
import os
import requests
from typing import Dict

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    CallbackContext,
    ConversationHandler
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
GENERAL_CONTEXT, WAITING_PHOTO = range(2)

# Callback data 
WANT_TO_ADD_PHOTO, WANT_QUOTE = range(2)


def _get_unix_timestamp() -> int:
    """Returns unix timestamp."""

    import time
    from datetime import datetime

    return int(time.mktime(datetime.now().timetuple()))


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Hi, I'm your helper bot")
    update.message.reply_text('Please choose:', reply_markup=markup())

    return GENERAL_CONTEXT


def markup() -> InlineKeyboardMarkup:
    keyboard = [
        [
         InlineKeyboardButton(text="GitHub", url='https://github.com/bilorukavsky/python_task'),
         InlineKeyboardButton(text="Quote", callback_data=str(WANT_QUOTE)),
        ],
        [InlineKeyboardButton(text="Add a photo", callback_data=str(WANT_TO_ADD_PHOTO))],
    ]
    return InlineKeyboardMarkup(keyboard)


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I'm your helper bot")


def upload_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user

    photo_file = update.message.photo[-1].get_file()
    photo_file.download(f'photos/{user.id}_{_get_unix_timestamp()}.jpg')

    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('Photo added')

    update.message.reply_text('Please choose:', reply_markup=markup())
    return GENERAL_CONTEXT


def quote() -> Dict:
    with requests.get('https://zenquotes.io/api/random') as r:
        if r.status_code == 200:
            response = r.json()
            return response
        else:
            r.raise_for_status()


def want_to_add_photo(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    query.edit_message_text("Upload a photo:")
    return WAITING_PHOTO


def want_quote(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    response = quote()
    query.edit_message_text(f"Quote: {response[0]['q']}")
    query.message.reply_text(f"Author: {response[0]['a']}")

    query.message.reply_text('Please choose:', reply_markup=markup())


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""

    update.message.reply_text("Окей")
    return ConversationHandler.END


def main() -> None:
    updater = Updater(os.environ["TOKEN"])

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("help", help_command))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            GENERAL_CONTEXT: [
                CallbackQueryHandler(want_to_add_photo, pattern='^' + str(WANT_TO_ADD_PHOTO) + '$'),
                CallbackQueryHandler(want_quote, pattern='^' + str(WANT_QUOTE) + '$'),
                MessageHandler(Filters.all & ~Filters.command, echo)
                ],
            WAITING_PHOTO: [
                MessageHandler(Filters.photo, upload_photo)
                ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        name="repeating_bot_context",
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()