# Yatube_api
yatube_api это простой api для проекта yatube написанный на python 3.7 c помощью библиотеки Django REST framework.

## Как запустить проект:
###### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```
cd api_final_yatibe
###### Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
###### Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
###### Выполнить миграции:
```
python3 manage.py migrate
```
###### Запустить проект:
```
python3 manage.py runserver
```
