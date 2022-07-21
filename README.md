# Spacey
- Подготовка
    ```
    pip install -r requirements.txt
    ```
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