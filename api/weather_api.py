import requests
from config import config

weather_key = config.weather_key


def weather_handler(name):
    try:
        city = name
        url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}'.format(
            city=city, api_key=weather_key)

        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        clouds = weather_data['weather'][0]['description']
        temp_min = round(weather_data['main']['temp_min'])
        temp_max = round(weather_data['main']['temp_max'])
        wind_speed = round(weather_data['wind']['speed'])

        return 'Сейчас в городе {city}: {temp_c}°C\nОщущается как: {temp_f}°C\n{clouds}\n' \
               'Минимальная температура достигнет: {tmin}°C\nМаксимальная: {tmax}°C\n' \
               'Скорость ветра: {wind} м/с\n'.format(
            city=city, temp_c=temperature, temp_f=temperature_feels,
            clouds=clouds.capitalize() + '.', tmin=temp_min, tmax=temp_max, wind=wind_speed)

    except KeyError:
        return 'Это какой то неизвестный мне город...\nВы точно правильно написали название?'
    except Exception:
        return 'Упс, ошибочка... Похоже что-то с соединением к сервису погоды.\n' \
               'Такое бывает, попробуйте ещё раз чуть позднее.'
