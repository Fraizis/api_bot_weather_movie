import requests
from config import config

movie_key = config.movie_key


def top_movies_handler(message):
    try:
        url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/collections?type=TOP_250_MOVIES&page={page}".format(
            page=message)
        headers = {
            'X-API-KEY': f'{movie_key}',
            'Content-Type': 'application/json',
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        for item in data['items']:
            yield ('{posterUrlPreview}. Название: {nameRu}. Рейтинг: Kinopoisk: {ratingKinopoisk}. '
                   'IMDB: {ratingImdb}. Жанр: {genres}. Год: {year}').format(
                posterUrlPreview=item['posterUrlPreview'],
                nameRu=item['nameRu'],
                ratingKinopoisk=item['ratingKinopoisk'],
                ratingImdb=item['ratingImdb'],
                genres=item['genres'][0]['genre'],
                year=item['year']
            )

    except requests.exceptions.ConnectionError:
        return 'Что-то с интернетом...'

    except Exception:
        return 'Упс...Что-то пошло не так.'


def movie_handler(message):
    try:
        url = "https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=ALL&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&keyword={movie}&page=1".format(
            movie=message)

        headers = {
            'X-API-KEY': f'{movie_key}',
            'Content-Type': 'application/json',
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        for movie in data['items']:
            yield ('\nНазвание: {nameRu}\nПостер: {posterUrlPreview}\nТип: {genres}\n'
                   'Рейтинг: Kinopoisk: {ratingKinopoisk}, Imdb: {ratingImdb}\nГод: {year}').format(
                nameRu=movie['nameRu'],
                posterUrlPreview=movie['posterUrlPreview'],
                genres=movie['genres'][0]['genre'],
                ratingKinopoisk=movie['ratingKinopoisk'],
                ratingImdb=movie['ratingImdb'],
                year=movie['year']
            )

    except KeyError:
        return 'По вашему запросу ничего не найдено.\nПроверьте правильность названия фильма.'
    except Exception:
        return 'Упс...Что-то пошло не так..'
