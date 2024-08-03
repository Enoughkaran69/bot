import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your Telegram Bot token
TOKEN = '6299534774:AAGMAEGxEiY8lvglLkuPE5WzVk0FGfibuw0'

# Function to get a random message from the web service
def get_random_message():
    response = requests.get('https://bot-4my0.onrender.com/random_message')
    if response.status_code == 200:
        return response.json().get('message')
    else:
        return "Error fetching message"

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a message, and I will reply with a random message.')

# Message handler
def handle_message(update: Update, context: CallbackContext) -> None:
    random_message = get_random_message()
    update.message.reply_text(random_message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

