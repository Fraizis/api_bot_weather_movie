import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

bot_token = os.getenv('bot_token')
weather_key = os.getenv('weather_key')
movie_key = os.getenv('movie_key')
