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
            telegram.sendImage(bot, os.environ["TELEGRAM_CHANNEL_ID"], imageToPost)
            time.sleep(int(os.environ["PUBLISH_TIME"]))
        imageList = random.shuffle(imageList)

def main():
    load_dotenv(".env")
    load_dotenv(".secure/.env")
    NASA_API_KEY = os.environ['NASA_API_KEY']

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

    date = epic.get_epic_dates(NASA_API_KEY)[0]
    image_id = epic.get_epic_image_ids(NASA_API_KEY, date)[0]
    url, params = epic.get_epic_image_url(NASA_API_KEY, date, image_id)
    download.download_image(url, os.path.join("images", "epic-{}-{}.png".format(date, image_id)), params)

    imageList = []
    
    for index, image_url in enumerate(apod.get_apod_urls(NASA_API_KEY, 40)):
        extention = os.path.splitext(image_url)[1]
        filename = os.path.join("images", "nasa_apod_{}{}".format(index, extention))
        print("Downloading", filename)
        download.download_image(image_url, filename)
        imageList.append(filename)
        
    for index, image_url in enumerate(spacex.get_flight_images("5eb87d47ffd86e000604b38a")):
        extention = os.path.splitext(image_url)[1]
        filename = os.path.join("images", "nasa_spacex_{}{}".format(index, extention))
        print("Downloading", filename)
        download.download_image(image_url, filename)
        imageList.append(filename)
    print("Done")
    random.shuffle(imageList)
    post_forever(bot, imageList)


if __name__ == "__main__":
    main()