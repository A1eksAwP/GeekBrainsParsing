import secret
import requests
import json
from pprint import pprint

api_key = secret.api_key #'k_vasgl123'
lang = 'en'
url = f'https://imdb-api.com/{lang}/API/Top250Movies/{api_key}'
top250 = requests.get(url)
data = top250.json()
film = data['items']

with open('IMBDb250.json', 'a', encoding='utf-8') as outfile:
    json.dump(f"Answer for your request to IMBDb: {film}", outfile)

print(f"\nОтвет от сервера: {top250.status_code}\n")
print(f"Количество найденных фильмов: {len(film)}\n")

film_rank = 0
while film_rank < len(film):
    print(f"Фильм {film_rank + 1}-й: '{film[film_rank]['title']}', его оценка: {film[film_rank]['imDbRating']}, фильм был выпущен в {film[film_rank]['year']} году;")
    film_rank += 1

user_choose = int(input("\nО каком фильме хочешь узнать подробнее?\n"))
while user_choose != 0:
    if user_choose <= len(film) and user_choose > 0:
        pprint(film[user_choose-1])
        user_choose = int(input("\nХочешь узнать еще о каком-то фильме из списка? Для выхода введи '0':\n"))
    else:
        user_choose = int(input("\nТакого номера фильма в списке нет, попробуй другой:\n"))

print("Спасибо за использование программы, киноман, смотри только лучшее!")