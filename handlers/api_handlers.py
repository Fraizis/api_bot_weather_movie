from api import weather_api, movie_api
from handlers.commands import bot, types, user_states, queries, datetime


@bot.message_handler(func=lambda message: True)
def self_states(message):
    cur_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    queries.user_create(message.from_user.id, message.text, cur_time)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('🌦 Погода')
    button_2 = types.KeyboardButton('🍿 Поиск фильмов')
    keyboard.add(button_1, button_2)

    keyboard_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('🌦 Погода')
    button_2 = types.KeyboardButton('🍿 Поиск фильмов')
    button_3 = types.KeyboardButton('🥤 Рейтинг фильмов')
    keyboard_1.add(button_1, button_2, button_3)

    if message.text == '🌦 Погода':
        user_states['user'] = 'weather'
        bot.send_message(message.chat.id, 'Введите название города и я скажу вам какая там сейчас погода:',
                         reply_markup=keyboard)

    elif message.text == '🍿 Поиск фильмов':
        user_states['user'] = 'movies'
        bot.send_message(message.chat.id, 'Какой фильм будем искать?\n'
                                          'Введите название фильма на английском языке:\n(Пример: Batman)',
                         reply_markup=keyboard_1)

    elif user_states['user'] == 'weather':
        city = weather_api.weather_handler(message.text)
        bot.send_message(message.chat.id, city)
        bot.send_message(message.chat.id, '\nПосмотрим погоду в другом городе?\n'
                                          'Просто введите название:', reply_markup=keyboard)

    elif user_states['user'] == 'movies':
        if message.text == '🥤 Рейтинг фильмов':
            user_states['user'] = 'top-1000'
            bot.send_message(message.chat.id, 'Введите страницу (от 1-10) для показа лучших фильмов\n(Например: 1):',
                             reply_markup=keyboard_1)

        else:
            search = movie_api.movie_handler(message.text)
            for num in search:
                bot.send_message(message.chat.id, num)
            bot.send_message(message.chat.id, 'Поищем другой фильм?', reply_markup=keyboard_1)

    elif user_states['user'] == 'top-1000':
        answer = movie_api.top_movies_handler(message.text)
        for num in answer:
            bot.send_message(message.chat.id, num)
        bot.send_message(message.chat.id, 'Показать другую страницу?\nПросто введите номер от 1 до 10:',
                         reply_markup=keyboard_1)


