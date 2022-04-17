import requests
import json

user = input('Для получения списка репозиториев введите ник пользователя GitHub: \n')
url = f'https://api.github.com/users/{user}/repos'
user_repo = requests.get(url)
data = user_repo.json()

print(f"\nОтвет от сервера: {user_repo.status_code}\n")
if user_repo.ok:
    print(f"Пользователь {user} найден, у него содержится {len(data)} открытых репозиториев! \n")
    repo = 0
    while repo < len(data):
        print(f"Ссылка на {repo + 1}-й репозиторий: {data[repo]['svn_url']}")
        repo += 1
else:
    print(f"К сожалению, пользователь с ником {user} на платформе GitHub еще не существует")

with open('github_repo.json', 'w', encoding='utf-8') as outfile:
    json.dump(f"Answer for your request to {user}: {data}", outfile)

print('Мы любезно записали тебе в файл "github_repo.json" вывод последнего результата! Спасибо за использование программы!')