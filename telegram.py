import telepot
import argparse
import glob
import random

def initBot(token):
    return telepot.Bot(token)

def sendImage(bot, channelId, photoPath):
    with open(photoPath, "br") as f:
        bot.sendPhoto(channelId, f)