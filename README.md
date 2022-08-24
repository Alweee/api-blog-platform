# Yatube_api
yatube_api это простой api для проекта yatube написанный на python 3.7 c помощью библиотеки Django REST framework.

### Список некоторых используемых технологий/пакетов:

* python==3.7.8
* djangorestframework==3.12.4
* Pillow==8.3.1
* PyJWT==2.1.0
* djangorestframework-simplejwt==4.7.2
* djoser
* django_filters

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Alweee/api-blog-platform.git
```

```
cd api-blog-platform
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv

```

```
source venv/bin/activate
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
Пример ответа:
{
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
Пример запроса:
{
"text": "string"
}
```

```
Пример ответа:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
