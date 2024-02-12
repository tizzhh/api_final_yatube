### API для yatube
API версии 1 для взаимодействия с сервисом yatube. Доступны следующие эндпоинты:
```
posts/
posts/<int:pk>/
posts/<int:pk>/comments/
posts/<int:pk>/comments/<int:pk>
groups/
groups/<int:pk>
follow/
``` 

Для аутентификации используется JWT и Djoser
```
jwt/create/
jwt/refresh/
jwt/verify/
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:tizzhh/api_final_yatube.git
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

### Примеры запросов
Полная документация доступна по эндпоинту *redoc/*

- GET api/v1/posts

Ответ:
```
[
    {
        "id": 2,
        "author": "user",
        "text": "test_post",
        "pub_date": "2024-02-10T19:54:48.228516Z",
        "image": null,
        "group": null
    },
    {
        "id": 3,
        "author": "user",
        "text": "aboba",
        "pub_date": "2024-02-10T22:41:08.498577Z",
        "image": null,
        "group": null
    },
    ...
]
```
- GET api/v1/posts/?limit=1&offset=1

Ответ:
```
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/posts/?%3Foffset=1&limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": 2,
            "author": "user",
            "text": "test_post",
            "pub_date": "2024-02-10T19:54:48.228516Z",
            "image": null,
            "group": null
        }
    ]
}
```
- GET api/v1/posts/<int:pk>/comments/

Ответ:
```
[
    {
        "id": 1,
        "author": "user",
        "text": "test_comment",
        "created": "2024-02-10T20:11:03.041477Z",
        "post": 2
    }
]
```
- GET api/v1/follow/

Ответ:
```
[
    {
        "user": "user",
        "following": "user2"
    }
]
```

Используемые библиотеки:
- Django==3.2.16
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==9.3.0
- PyJWT==2.1.0
- requests==2.26.0
- djoser==2.1.0

Версия Python:
Python 3.9.18

Автор:

> tizzhh  https://github.com/tizzhh

> darovadraste@gmail.com

> tizzhh.github.io