import telepot
import argparse
import glob
import random

def initBot(token):
    return telepot.Bot(token)

def sendImage(bot, channelId, photoPath):
    with open(photoPath, "br") as f:
        bot.sendPhoto(channelId, f)

def main():
    parser = argparse.ArgumentParser(
        description='Tool for sending images to telegram.')
    parser.add_argument('--channel-id', type=str, 
                        help='Telegram channel id', required=True)
    parser.add_argument('--image-path', type=str,
                        help='Image path or glob mask', required=True)
    parser.add_argument('--token', type=str, help='Telegram token', required=True)
    
    args = parser.parse_args()

    bot = initBot(args.token)
    images = glob.glob(args.image_path)
    sendImage(bot, args.channel_id, random.choose(images))

if __name__ == "__main__":
    main()