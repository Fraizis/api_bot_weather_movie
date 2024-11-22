import requests
from config import config

rapid_key = config.rapid_key


def top_movies_handler(message):
    try:
        url_2 = "https://imdb-top-1000-movies-series.p.rapidapi.com/list/{page}".format(page=message)
        headers_2 = {
            "x-rapidapi-key": "{key}".format(key=rapid_key),
            "x-rapidapi-host": "imdb-top-1000-movies-series.p.rapidapi.com"
        }

        response = requests.get(url_2, headers=headers_2)
        answer = response.json()
        for movie in answer['result']:
            yield '{rank}. {title}. Рейтинг: {rate}. Жанр: {genre}. Год: {year}. ({star_1}, {star_2})'.format(
                rank=movie['rank'], title=movie['Series_Title'], year=movie['Released_Year'],
                star_1=movie['Star1'], star_2=movie['Star2'], genre=movie['Genre'],
                rate=movie['IMDB_Rating'])
    except Exception:
        return 'Упс...Что-то пошло не так.'


def movie_handler(message):
    try:
        search = message
        url = "https://imdb-com.p.rapidapi.com/auto-complete"
        querystring = {'query': '{search}'.format(search=search)}

        headers = {
            "x-rapidapi-key": '{key}'.format(key=rapid_key),
            "x-rapidapi-host": "imdb-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        for movie in data['data']['d']:
            yield '\nНазвание: {name}\nПостер: {image}\nТип: {type}\nРейтинг: {rank}\n' \
                  'В главных ролях: {stars}\nГод: {year}'.format(
                                 image=movie['i']['imageUrl'], name=movie['l'], type=movie['qid'],
                                 rank=movie['rank'], stars=movie['s'], year=movie['y'])
    except KeyError:
        return 'По вашему запросу ничего не найдено.\nПроверьте правильность названия фильма.'
    except Exception:
        return 'Упс...Что-то пошло не так..'




