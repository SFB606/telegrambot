import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define your bot token obtained from BotFather
TOKEN = 'your_bot_token_here'

# Define the command handler function for /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Telegram bot.')

# Define the message handler function
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Create an instance of the Updater class
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler for /start command
    dispatcher.add_handler(CommandHandler("start", start))

    # Register the message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
