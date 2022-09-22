import dotenv
import requests
import argparse
import os
import random

from download import download_image

def build_url(url, params):
    if params:
        url += "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    return url

def get_epic_image_ids(api_key, date):
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params = {"api_key":api_key})
    response.raise_for_status()
    return [apod["image"] for apod in response.json()]

def get_epic_image_and_params(api_key, date, image_id):
    return "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(date, image_id), {"api_key":api_key}

def main():
    if os.path.exists(".secure/.env"):
        dotenv.load_dotenv(".secure/.env")

    parser = argparse.ArgumentParser(
        description='Tool for downloading NASA EPIC images.')
    parser.add_argument('--date', default=None, type=str, help='Date to download')
    parser.add_argument('--no-download', default=None, type=str, help='Do not download image')

    args = parser.parse_args()

    api_key = os.environ.get("NASA_API_KEY", None)
    if not api_key:
        parser.print_help()
        print("ERROR: specify API_KEY (in .env)")
        exit(1)

    if not args.date or not args.image_id:
        parser.print_help()
        print("ERROR: --date and --image_id is required for --get-images")
        exit(1)
    image_id = random.choice(get_epic_image_ids(args.date))
    url, params = get_epic_image_and_params(api_key, args.date, image_id)
    print(build_url(url, params))
    extention = os.path.splitext(url)[1]
    if not args.no_download:
        os.makedirs("images", exist_ok=True)
        download_image(url, os.path.join("images", "epic-{args.date}-{args.image_id}{extention}"))

if __name__ == '__main__':
    main()