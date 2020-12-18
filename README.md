# foodgram-project
foodgram-project
Для загрузки тестовой базы воспользуйтесь командой "py manage.py load_data"

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
TELEGRAM_TOKEN=Токен Вашего бота в телеграме'''