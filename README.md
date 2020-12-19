![foodgram](https://github.com/TheZavitaev/foodgram-project/workflows/foodgram/badge.svg)
# foodgram-project
https://da-eda.ga/


foodgram-project


Для работы CI\CD необходимо добавить в гитхаб секреты:
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=блинный джанговский секреткей
IP=IP вашего сервера,
DOMAIN=ваш домен
DEBUG=True
DOCKER_USERNAME=Ваш никнейм на докерхабе
DOCKER_PASSWORD=ваш пароль от докерхаба
USER=юзернейм на сервере
SSH_KEY=-----BEGIN OPENSSH PRIVATE KEY-----Не забывайте, что эти штуки тоже относятся к приваткею-----END OPENSSH PRIVATE KEY-----
SSH_PORT=по умолчанию 22, есть вариант открыть другой порт на сервере и пользоваться им
TELEGRAM_TO=Ваш id в телеграме
TELEGRAM_TOKEN=Токен Вашего бота в телеграме

Запускаем процесс сборки и запуска контейнеров:

docker-compose up
Запускаем терминал внутри контейнера (на вин системах используйте winpty docker-compose exec web bash ):

docker-compose exec web bash
Накатываем миграции:

python manage.py migrate

Собираем статику:

python manage.py collectstatic --no-input

Для создания администратора воспользуйтесь командой:

python manage.py createsuperuser

Для загрузки базы ингредиентов воспользуйтесь командой:

python manage.py load_data
