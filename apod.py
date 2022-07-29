import requests
import argparse
import os

from download import download_image

def get_apod_urls(api_key, count):
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params={"api_key": api_key, "count": count})
    response.raise_for_status()
    return [apod["url"] for apod in response.json()]


def main():
    parser = argparse.ArgumentParser(
        description='Tool for downloading NASA APOD images.')
    parser.add_argument("--count", default=1, help="Image count")
    parser.add_argument("--api-key", type=str, help="NASA Api key", required=True)
    parser.add_argument('--no-download', default=False,
                        action="store_true", help='Do not download photos')

    args = parser.parse_args()

    urls = get_apod_urls(args.api_key, args.count)
    if not args.no_download:
        for index, url in enumerate(urls):
            extention = os.path.splitext(url)[1]
            download_image(url, f"apod-{index}{extention}")

    print(url)
    
if __name__ == "__main__":
    main()