from dotenv import load_dotenv
import requests
import os
import random
import time

import telegram
import epic, apod, spacex, download

os.makedirs("images", exist_ok=True)


def post_forever(bot, imageList, chId, pTime):
    while True:
        for imageToPost in imageList:
            try:
                telegram.sendImage(bot, chId, imageToPost)
                time.sleep(int(pTime))
            except (ConnectionError) as e:
                print("Error occured\n", "{}: {}".format(type(e).__name__, e))
                time.sleep(1)
        imageList = random.shuffle(imageList)


def main():
    load_dotenv(".env")
    load_dotenv(".secure/.env")

    publish_time = os.environ["PUBLISH_TIME"]

    bot = telegram.initBot(os.environ["TELEGRAM_TOKEN"])

    imageList = [os.path.join("images", filename) for filename in os.listdir("images")]
    random.shuffle(imageList)
    post_forever(bot, imageList, os.environ["TELEGRAM_CHANNEL_ID"], publish_time)


if __name__ == "__main__":
    main()
