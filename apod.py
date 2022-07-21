import requests
import argparse

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

    args = parser.parse_args()

    print(get_apod_urls(args.api_key, args.count))
    
if __name__ == "__main__":
    main()