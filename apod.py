import dotenv
import requests
import argparse
import os

from download import download_image

def get_apod_urls(api_key, count):
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params={"api_key": api_key, "count": count})
    response.raise_for_status()
    return [apod["url"] for apod in response.json() if apod["media_type"]=="image"]


def main():
    if os.path.exists(".secure/.env"):
        dotenv.load_dotenv(".secure/.env")

    parser = argparse.ArgumentParser(
        description='Tool for downloading NASA APOD images.')
    parser.add_argument("--count", default=1, help="Image count")
    parser.add_argument("--api-key", type=str, help="NASA Api key", required=False)
    parser.add_argument('--no-download', default=False,
                        action="store_true", help='Do not download photos')

    args = parser.parse_args()

    api_key = args.api_key
    if not api_key:
        api_key = os.environ.get("NASA_API_KEY", None)
        if not api_key:
            parser.print_help()
            print("ERROR: specify API_KEY (in .env)")
            exit(1)

    urls = get_apod_urls(api_key, args.count)
    if not args.no_download:
        for index, url in enumerate(urls):
            extention = os.path.splitext(url)[1]
            os.makedirs("images", exist_ok=True)
            download_image(url, os.path.join("images", f"apod-{index}{extention}"))

    print(urls)
    
if __name__ == "__main__":
    main()