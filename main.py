from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot import *

TOKEN: Final = '6731666250:AAE9ukrzSYgy9s2V6ke9mT2JoUPVgvyB3FQ'
BOT_USERNAME : Final = "@mehdi_ssh_test_bot"

if __name__ == '__main__':

    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, command_handler))

    # Errors
    #app.error_handlers(error)

    print("Polling...")
    app.run_polling(poll_interval=3)