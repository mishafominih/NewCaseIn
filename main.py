from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import os
import Db_Init

# PORT = int(os.environ.get('PORT'))
# TOKEN = os.environ.get('TOKEN')
# URL = os.environ.get('URL')
updater = Updater(token='1694016582:AAGobMt3d3mruS_1sB7DFHqSm2UPt9zYKuU', use_context=True)
dispatcher = updater.dispatcher
Db_Init.init()

CHOOSING_OPTION, QUIZES, START_OVER = range(3)


def start(update: Update, context : CallbackContext):
    if not context.user_data.get(START_OVER):
        # Добавить проверку, есть ли пользователь уже в бд, чтобы не выводить лишнее сообщение при нажатии кнопки назад
        context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот Атом, если ты новый сотрудник "
                                                                        "корпорации как РосАтом, то я могу помочь тебе в "
                                                                        "адаптации в нашем большом и дружном коллективе)")
    # Добавление в бд
    markup = [
        ['Зарплата за месяц', 'Зарплата за год'],
        ['Твоя карьерная лестница'],
        ['Инфа о нас'],
        ['Карта офисов нашей компании']
    ]
    keyboard = ReplyKeyboardMarkup(markup, one_time_keyboard=False)
    update.message.reply_text(text="Выбери, что ты хочешь узнать. В разделе \"инфа о "
                                   "нас\" есть сного важной и интересной информации "
                                   "о РосАтоме и опросы по ней. Лучших по ним ждут "
                                   "небольшие призы)", reply_markup=keyboard)
    context.user_data[START_OVER] = False
    return CHOOSING_OPTION


def monthly_payment(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='35000 рублей')  # Достать данные по зп из бд


def yearly_payment(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='420000 рублей')  # Достать данные по зп из бд


def carreer(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='1,2,3,4(тут),5')  # Достать из бд


def offices(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='https://rosatom.ru/about/factories/')


def unknown_answer(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ой, я не могу понять твой ответ, ты уверен,'
                                                                    'что всё правлиьно написал?')


def back_to_start(update: Update, context: CallbackContext):
    start(update, context)
    return CHOOSING_OPTION


def quizes(update: Update, context):
    markup = [
        ['О безопасности', 'О культуре нашей компании'],
        ['Викторина о безопасности'],
        ['Викторина о культуре'],
        ['Назад']
    ]
    keyboard = ReplyKeyboardMarkup(markup, one_time_keyboard=False)
    update.message.reply_text(text='В данном разделе ты можешь прочитать различную информацию о нашей компании и пройти'
                                   'викторины, посоревновавшись с другими новыми сотрудниками', reply_markup=keyboard)
    return QUIZES


# def cancel(update: Update, context):
#


choosing_option_handlers = [
    MessageHandler(Filters.regex('Зарплата за месяц$'), monthly_payment),
    MessageHandler(Filters.regex('Зарплата за год$'), yearly_payment),
    MessageHandler(Filters.regex('Твоя карьерная лестница$'), carreer),
    MessageHandler(Filters.regex('Карта офисов нашей компании$'), offices),
    MessageHandler(Filters.regex('Инфа о нас$'), quizes)]

conv_handler_starting = ConversationHandler(entry_points=[CommandHandler('start', start)],
                                            fallbacks=[MessageHandler(Filters.text, unknown_answer)],
                                            states={
                                                CHOOSING_OPTION: choosing_option_handlers,
                                                QUIZES: [MessageHandler(Filters.regex('Назад$'), back_to_start)]})
dispatcher.add_handler(conv_handler_starting)

# updater.start_webhook(listen="0.0.0.0",
#                       port=PORT,
#                       url_path=TOKEN)
# updater.bot.set_webhook(URL + TOKEN)
updater.start_polling()
updater.idle()
