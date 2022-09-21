# API Blog-platform

### Описание:
API для всех моделей приложения `Posts`.

Аутентификация по токену. `JWT + Djoser`.

API написан на `ViewSets`.

### Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Simple%20JWT-%20-008080)](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
[![Python](https://img.shields.io/badge/djoser-%20-008080)](https://djoser.readthedocs.io/en/latest/index.html)
[![](https://img.shields.io/badge/Pillow-%20-008080)](https://pypi.org/project/Pillow/)
[![](https://img.shields.io/badge/django--filter-%20-008080)](https://django-filter.readthedocs.io/en/stable/guide/usage.html)

## Как запустить проект:
**Клонировать репозиторий и перейти в него в командной строке:**

`git clone https://github.com/Alweee/api-blog-platform.git`

`cd yatube_api` 

**Cоздать и активировать виртуальное окружение:**

`python -m venv venv`

`source venv/bin/activate`

**Установить зависимости из файла requirements.txt:**

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

**Выполнить миграции:**

`python manage.py migrate`

**Запустить проект:**

`python manage.py runserver`

## Примеры запросов:
**`GET` | Получить информацию о группе: `/api/v1/groups/2/`**

Response:
```
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 
```

**`POST` | Добавление нового поста: `/api/v1/posts/`**

Request:
```
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре.",
    "group": 1
} 
```

Response:
```
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 
```

**`POST` | Отправляем новый комментарий к посту с id=14: `/api/v1/posts/14/comments/`**

Request:
```
{
    "text": "тест тест"
} 
```

Response:
```
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```
