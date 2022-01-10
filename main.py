import telegram.ext
import responses
import os

PORT = int(os.environ.get('PORT',80))
with open('key.txt','r') as f:
    TOKEN = f.read()

# print(TOKEN)

def start(update,context):
    update.message.reply_text('Welocme to Shadow Bot!')

def help(update,context):
    update.message.reply_text('''
    The following commands are available:
    /start -> Welcome message
    /help -> This Message
    /content -> Information about me
    /contact -> Information about Contact
    ''')


def content(update,context):
    update.message.reply_text('I am wikipedia in myself!')

def contact(update,context):
    update.message.reply_text('You can contact my owner via Email at botsb4882@gmail.com')


def handle_message(update,context):
    update.message.reply_text(responses.get_response(update.message.text))


def main():
    updater = telegram.ext.Updater(TOKEN,use_context=True)

    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler('start',start))
    disp.add_handler(telegram.ext.CommandHandler('help',help))
    disp.add_handler(telegram.ext.CommandHandler('content',content))
    disp.add_handler(telegram.ext.CommandHandler('contact',contact))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))

    #updater.start_polling()
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,webhook_url='https://helperbotforyou.herokuapp.com/' + TOKEN)
    #updater.bot.setWebhook('https://helperbotforyou.herokuapp.com/' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

