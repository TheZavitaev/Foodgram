name: foodgram

on: [push]

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        pip install -r requirements.txt

    - name: Lint with flake8
      run: flake8 . --config=setup.cfg

    - name: Test with pytest
      run: pytest

  build_and_push_to_docker_hub:
    name: Push Docker image to Docker Hub
    runs-on: ubuntu-latest
    needs: tests
    steps:
      - name: Check out the repo
        uses: actions/checkout@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1

      - name: Login to Docker
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Push to Docker Hub
        uses: docker/build-push-action@v2
        with:
          push: true
          tags: thezavitaev/foodgram:latest

  deploy:
    runs-on: ubuntu-latest
    needs: build_and_push_to_docker_hub
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
            python-version: 3.8

      - name: Install dump-env and create .env
        env:
          SECRET_DB_ENGINE: ${{ secrets.DB_ENGINE }}
          SECRET_DB_NAME: ${{ secrets.DB_NAME }}
          SECRET_POSTGRES_USER: ${{ secrets.POSTGRES_USER }}
          SECRET_POSTGRES_PASSWORD: ${{ secrets.POSTGRES_PASSWORD }}
          SECRET_DB_HOST: ${{ secrets.DB_HOST }}
          SECRET_DB_PORT: ${{ secrets.DB_PORT }}
          SECRET_SECRET_KEY: ${{ secrets.SECRET_KEY }}
        run: |
          python -m pip install --upgrade pip
          pip install dump-env
          dump-env --template=.env.template --prefix='SECRET_' > .env
      - name: Copy file via ssh password
        uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USER }}
          key: ${{ secrets.SSH_KEY }}
          port: ${{ secrets.SSH_PORT }}
          source: "./.env, nginx/default.conf, ./docker-compose.yaml"
          target: "/home/thezavitaev/code"

      - name: Executing remote ssh commands to deploy
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USER }}
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd ~
            cd ./code
            sudo docker rmi thezavitaev/foodgram -f
            sudo docker pull thezavitaev/foodgram:latest
            sudo docker-compose up --force-recreate -d web
  send_message:
    runs-on: ubuntu-latest
    needs: deploy
    steps:
      - name: send message
        uses: appleboy/telegram-action@master
        with:
          to: ${{ secrets.TELEGRAM_TO }}
          token: ${{ secrets.TELEGRAM_TOKEN }}
          message: ${{ github.workflow }} поднят!