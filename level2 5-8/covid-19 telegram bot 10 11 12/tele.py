#pip install python-telegram-bot
# pip3 install python-telegram-bot
#python -m pip install --upgrade pip
# file name should not be telegram.py it should be other then that
from telegram.ext import Updater, CommandHandler
API_KEY="2038731411:AAGGYcZ_pL_8vOh2O7SWvmSW69egryBEdzc"

#updater variable update whatever we update in our bot
# accept two parameter
updater = Updater(token=API_KEY, use_context=True) #Replace TOKEN with your token string

#dispatcher variable dispatch the update to our bot
dispatcher = updater.dispatcher

def hello(update, context):
    # chat_id, text is predefined you cannot change the name
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, How r u?')


#which command do (or run) which function
hello_handler = CommandHandler('hello', hello)

# update our dispatcher, we are adding a handler for hello command /hello
dispatcher.add_handler(hello_handler)
# start polling so that our program see upcoming message


def motionD(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='https://www.youtube.com/watch?v=oxmZ9zczptg')

motionD_handler = CommandHandler('motionDEtection', motionD)
dispatcher.add_handler(motionD_handler)













updater.start_polling()
