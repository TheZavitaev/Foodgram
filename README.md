![foodgram](https://github.com/TheZavitaev/foodgram-project/workflows/foodgram/badge.svg)

# **[Da-Eda-project](84.201.176.31)**

![Banner](/static/banner.jpg)
Выпускной проект программы Яндекс.Практикум **[Python-разработчик](https://praktikum.yandex.ru/backend-developer/)**

Da-eda - это сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное 
и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям 
создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

##Quick-start

Для работы, Вам необходимо иметь установленную версию **[Python](https://www.python.org/)** версии 3.8 и выше, **[Docker](https://www.docker.com/)**, **[Docker-Compose](https://docs.docker.com/compose/)**. 

```
Клонируем репозиторий на локальную машину и перейдите в рабочую директорию:
git clone https://github.com/TheZavitaev/infra_sp2.git && cd infra_sp2

В корневой папке находим файл .env.template. 
По образу и подобию необходимо создать файл .env и заполнить его своими значениями.

Запускаем процесс сборки и запуска контейнеров:
docker-compose up 

Запускаем терминал внутри контейнера (на вин системах используйте winpty docker-compose exec web bash):
docker-compose exec web bash

Накатываем миграции:
python manage.py migrate

Собираем статику:
python manage.py collectstatic --no-input

Для создания администратора воспользуйтесь командой:
python manage.py createsuperuser

Для загрузки базы ингредиентов воспользуйтесь командой:
python manage.py load_data
```

#### После этого все манипуляции с сайтом вы можете совершать, перейдя по адресу: http://127.0.0.1/

## Технологии:
- **[Python](https://www.python.org/)**,
- **[Django](https://www.djangoproject.com/)**,
- **[PostgreSQL](https://www.postgresql.org/)**,
- **[NGINX](https://nginx.org/)**,
- **[Docker](https://www.docker.com/)**,
- **[Docker-Compose](https://docs.docker.com/compose/)**,
- **[GitHub Actions](https://github.com/actions)**.