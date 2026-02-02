import datetime
from telebot import types
from database.models import User
from loader import bot
from database import queries

user_states = {}


@bot.message_handler(commands=['start', 'help'])
def main_menu(message):
    user_states['user'] = 'main_menu'
    user_name = message.from_user.username
    cur_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    queries.user_create(message.from_user.id, message.text, cur_time)

    bot.send_message(message.chat.id, '👋 Привет, {username}! Я твой бот-помошник!'.format(username=user_name))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('🌦 Погода')
    button_2 = types.KeyboardButton('🍿 Поиск фильмов')
    keyboard.add(button_1, button_2)

    bot.send_message(message.chat.id, 'Желаете узнать погоду в вашем городе?\n'
                                      'Или может поискать интересный фильм?\n'
                                      'Выберите в меню ниже что вас интересует:', reply_markup=keyboard)


@bot.message_handler(commands=['history'])
def message_history(message):
    user_states['user'] = 'main_menu'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('🌦 Погода')
    button_2 = types.KeyboardButton('🍿 Поиск фильмов')
    keyboard.add(button_1, button_2)

    bot.send_message(message.chat.id, 'Показываю историю всех запросов и сообщений с ботом:')
    for user in User.select().where(User.user_id == message.from_user.id).order_by(User.date.desc()).limit(10):
        bot.send_message(message.chat.id, 'Id: {}. Сообщение: {}. Дата: {}'.format(
            user.user_id, user.user_message, user.date))

    bot.send_message(message.chat.id, '\nЖелаете узнать погоду в вашем городе?\n'
                                      'Или может поискать интересный фильм?\n'
                                      'Выберите в меню ниже что вас интересует:', reply_markup=keyboard)
