from dotenv import load_dotenv
import requests
import os
import random
import time

import telegram
import epic, apod, spacex, download

os.makedirs("images", exist_ok=True)
NASA_API_KEY = os.environ['NASA_API_KEY']

def main():
    load_dotenv(".env")
    load_dotenv(".secure/.env")

    bot = telegram.initBot(os.environ["TELEGRAM_TOKEN"])

    date = epic.get_epic_dates(NASA_API_KEY)[0]
    image_id = epic.get_epic_image_ids(NASA_API_KEY, date)[0]
    url, params = epic.get_epic_image_url(NASA_API_KEY, date, image_id)
    download.download_image(url, "images/epic-{}-{}.png".format(date, image_id), params)

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
    while True:
        for imageToPost in imageList:
            telegram.sendImage(bot, os.environ["TELEGRAM_CHANNEL_ID"], imageToPost)
            time.sleep(int(os.environ["PUBLISH_TIME"]))
        imageList = random.shuffle(imageList)


if __name__ == "__main__":
    main()