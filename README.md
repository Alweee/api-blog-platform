# Yatube_api
yatube_api это простой api для проекта yatube написанный на python 3.7 c помощью библиотеки Django REST framework.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```
```
cd api_final_yatibe
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
## Примеры запросов:
Получить список всех публикаций: api/v1/posts/
```
{
Пример ответа:
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
       {...}
   ]
}
```
Добавление нового комментария к публикации: api/v1/posts/{post_id}/comments/
```
{
Пример запроса:
"text": "string"
}
```
Response samples
```
{
Пример ответа:
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

