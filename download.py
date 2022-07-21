import requests
import argparse

def download_image(url, imgname, params={}):
    image_content = requests.get(url, params=params).content
    
    with open(imgname, "bw") as f:
        f.write(image_content)