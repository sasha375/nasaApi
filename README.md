# Spacey

- Описание
    Данный проект позволяет автоматизировать скачивание и публикацию фотографий космоса.

## main.py
- Установка
    Установите python>=3.0
    Установите Зависимости (в пункте Зависимости)
    Создайте .env файл (в пункте Зависимости)
- Описание
    ```
    Главный файл
    ```
- Возможности

    &#9744; Параметры командной строки

    &#9744; Использование как библииотеку python
- Запуск
    ```
    python main.py
    ```
- Зависимости
    - Библиотеки
        ```
        requests==2.27.1
        python-dotenv==0.9.1
        telepot==12.7
        ```
        (Установить можно с помощью
        ```
        python -m pip install -r requirements.txt
        ```
        )
    - .env
        ```
        PUBLISH_TIME=    СЕКУНДЫ_МЕЖДУ_ОТПРАВКАМИ
        ```
    - .secure/.env
        ```
        TELEGRAM_TOKEN= ТОКЕН_ТЕЛЕГРАМ [Где взять?](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)
        NASA_API_KEY=   ТОКЕН_НАСА [Где взять?](https://wilsjame.github.io/how-to-nasa/)
        TELEGRAM_CHANNEL_ID=     ID_ТЕЛЕГРАМ_КАНАЛА [Где взять?](https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel)
        ```
## telegram.py
- Описание
    ```
    Отправка фото в телеграм
    ```
- Возможности

    &#9745; Параметры командной строки

    &#9745; Использование как библииотеку python
- Запуск
    ```
    python telegram.py CHANNEL_ID IMAGE_PATH BOT_TOKEN
    ```
## apod.py
- Описание
    ```
    Скачивание APOD фото
    ```
- Возможности

    &#9745; Параметры командной строки

    &#9745; Использование как библииотеку python
- Запуск
    ```
    python apod.py [--count COUNT] --api-key NASA_API_KEY
    ```
## epic.py
- Описание
    ```
    Скачивание EPIC фото
    ```
- Возможности

    &#9745; Параметры командной строки

    &#9745; Использование как библииотеку python
- Запуск
    ```
    python epic.py [--get-dates] [--get-images --date DATE] [--get-image-url --date DATE --image-id IMAGE_ID] --api-key NASA_API_KEY
    ```
## spacex.py
- Описание
    ```
    Скачивание фото полётов SpaceX
    ```
- Возможности

    &#9745; Параметры командной строки

    &#9745; Использование как библииотеку python
- Запуск
    ```
    python spacex.py [--flight-id FLIGHT_ID] [--raw-json]
    ```