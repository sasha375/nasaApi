# Spacey

## main.py
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
    ```
    requests
    python-dotenv
    ```
    - .env
        ```
        PUBLISH_TIME=    СЕКУНДЫ_МЕЖДУ_ОТПРАВКАМИ
        ```
    - .secure/.env
        ```
        TELEGRAM_TOKEN= ТОКЕН_ТЕЛЕГРАМ
        NASA_API_KEY=   ТОКЕН_НАСА
        CHANNEL_ID=     ID_ТЕЛЕГРАМ_КАНАЛА
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
- Зависимости
    ```
    requests
    ```
## download.py
- Описание
    ```
    Скачивание фото
    ```
- Возможности

    &#9745; Параметры командной строки

    &#9745; Использование как библииотеку python
- Запуск
    ```
    python download.py IMAGE_URL IMAGE_PATH
    ```
- Зависимости
    ```
    requests
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
- Зависимости
    ```
    requests
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
- Зависимости
    ```
    requests
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
    python spacex.py --flight-id FLIGHT_ID [--raw-json] --api-key SPACEX_API_KEY
    ```
- Зависимости
    ```
    requests
    ```
## url_builder.py
- Описание
    ```
    Утилита для отображения ссылки
    ```
- Возможности

    &#9744; Параметры командной строки

    &#9745; Использование как библииотеку python
- Запуск
    ```
    ```
- Зависимости
    ```
    ```