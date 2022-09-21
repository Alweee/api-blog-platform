# API Blog-platform

### Описание:
API для всех моделей приложения `Posts`.

Аутентификация по токену. `JWT + Djoser`.

API написан `ViewSets`.

### Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Simple%20JWT-%20-008080)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
[![Python](https://img.shields.io/badge/djoser-%20-008080)](https://djoser.readthedocs.io/en/latest/index.html)

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
Получить список всех публикаций: `api/v1/posts/`

Ответ:
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {...}
     ]
}
```

Добавление нового комментария к публикации: `api/v1/posts/{post_id}/comments/`

Запрос:
```
{
    "text": "string"
}
```

Ответ:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
