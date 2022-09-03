import argparse
from dotenv import load_dotenv
import requests
import os
import random
import time

import telegram
import epic, apod, spacex, download

os.makedirs("images", exist_ok=True)

def post_forever(bot, imageList):
    while True:
        for imageToPost in imageList:
            try:
                telegram.sendImage(bot, os.environ["TELEGRAM_CHANNEL_ID"], imageToPost)
                time.sleep(int(os.environ["PUBLISH_TIME"]))
            except (ConnectionError, telegram.error.NetworkError) as e:
                print("Error occured\n", type(e).__name__+":", str(e))
                time.sleep(1)
        imageList = random.shuffle(imageList)

def main():
    load_dotenv(".env")
    load_dotenv(".secure/.env")

    parser = argparse.ArgumentParser()
    parser.add_argument("--publish-time", type=int, required=False)

    args = parser.parse_args()

    publish_time = os.environ.get("PUBLISH_TIME", None)
    if not publish_time:
        publish_time = args.publish_time
        if not publish_time:
            parser.print_help()
            print("ERROR: specify PUBLISH_TIME in .env or args")


    bot = telegram.initBot(os.environ["TELEGRAM_TOKEN"])

    imageList = os.listdir("images")
    random.shuffle(imageList)
    post_forever(bot, imageList)


if __name__ == "__main__":
    main()