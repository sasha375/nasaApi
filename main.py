from dotenv import load_dotenv
import os
import random
import time
import urllib3 

import telegram

def post_forever(bot, imageList, chId, pTime):
    while True:
        for imageToPost in imageList:
            try:
                telegram.send_image(bot, chId, imageToPost)
                time.sleep(int(pTime))
            except urllib3.exceptions.MaxRetryError as e:
                print("Error occurred\n", "{}: {}".format(type(e).__name__, e))
                time.sleep(1)
        random.shuffle(imageList)


def main():
    load_dotenv(".env")
    load_dotenv(".secure/.env")

    publish_time = os.getenv("PUBLISH_TIME", 14400)

    bot = telegram.init_bot(os.environ["TELEGRAM_TOKEN"])

    image_list = [os.path.join("images", filename) for filename in os.listdir("images")]
    random.shuffle(image_list)
    post_forever(bot, image_list, os.environ["TELEGRAM_CHANNEL_ID"], publish_time)


if __name__ == "__main__":
    main()
