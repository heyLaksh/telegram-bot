from telegram.ext import *
import credentials


print("Starting bruh...")

def start(update, context):
    update.message.reply_text('Hello there!!!!')


def help(update, context):
    update.message.reply_text('Bruh, why do you need help, are you stupid or something')


def custom(update, context):
    update.message.reply_text('Coming Soon!!!!!!!!!')


def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hey bruh'
    if 'how are you' in text:
        return 'im good, wbu'

    return 'idk that yet'


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}"')

    if message_type == 'group':
        if '@hellclock_bot' in text:
            new_text = text.replace('@hellclock_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused error: {context.error}')


if __name__ == '__main__':
    updater = Updater(credentials.token, use_context = True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('custom', custom))


    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idle()
