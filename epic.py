import dotenv
import requests
import argparse
import os
import random

import datetime

from download import download_image


def build_url(url, params):
    if params:
        url += "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    return url


def get_epic_image_ids(api_key, date_object):
    formatted_date = date_object.strftime("%Y-%m-%d")
    response = requests.get(
        f"https://api.nasa.gov/EPIC/api/natural/date/{formatted_date}",
        params={"api_key": api_key}
    )
    response.raise_for_status()
    return [apod["image"] for apod in response.json()]


def get_epic_image_and_params(api_key, date_object, image_id):
    formatted_date = date_object.strftime("%Y/%m/%d")
    return "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png"\
        .format(formatted_date, image_id), {"api_key": api_key}


def main():
    if os.path.exists(".secure/.env"):
        dotenv.load_dotenv(".secure/.env")

    parser = argparse.ArgumentParser(
        description='Tool for downloading NASA EPIC images.')
    parser.add_argument('--date',
                        default=None,
                        type=str,
                        help='Date to download')
    parser.add_argument('--no-download',
                        default=False,
                        type=bool,
                        action="set_true",
                        help='Do not download image')

    args = parser.parse_args()

    api_key = os.environ["NASA_API_KEY"]
    date_object = datetime.datetime.strptime(args.date, "%d-%m-%Y")

    image_ids = get_epic_image_ids(api_key, date_object)
    for image_id in image_ids:
        url, params = get_epic_image_and_params(api_key, date_object, image_id)
        print(build_url(url, params))
        extension = os.path.splitext(url)[1]
        if not args.no_download:
            os.makedirs("images", exist_ok=True)
            download_image(url, os.path.join("images", f"epic-{args.date}-{image_id}{extension}"), params={"api_key":api_key})

if __name__ == '__main__':
    main()