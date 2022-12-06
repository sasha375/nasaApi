from dotenv import load_dotenv

import telepot
import argparse
import glob
import random
import os

def init_bot(token):
    return telepot.Bot(token)

def send_image(bot, channelId, photoPath):
    with open(photoPath, "br") as f:
        bot.sendPhoto(channelId, f)

def main():
    load_dotenv(".secure/.env")
    load_dotenv(".env")

    parser = argparse.ArgumentParser(
        description='Tool for sending images to telegram.')
    parser.add_argument('--image-path', type=str,
                        help='Image path', default="images")
    
    args = parser.parse_args()

    bot = init_bot(os.environ["TELEGRAM_TOKEN"])
    send_image(bot, os.environ["TELEGRAM_CHANNEL_ID"], args.image_path)

if __name__ == "__main__":
    main()