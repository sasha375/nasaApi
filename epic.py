import datetime
import requests
import argparse

def build_url(url, params):
    if params:
        url += "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    return url

def get_epic_dates(api_key):
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/all", params={"api_key":api_key})
    response.raise_for_status()
    return [apod["date"] for apod in response.json()]

def get_epic_image_ids(api_key, date):
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}", params = {"api_key":api_key})
    response.raise_for_status()
    return [apod["image"] for apod in response.json()]

def get_epic_image_url(api_key, date, image_id):
    return "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(date, image_id), {"api_key":api_key}

def main():
    parser = argparse.ArgumentParser(
        description='Tool for downloading NASA EPIC images.')
    parser.add_argument('--get-dates', default=False,
                        action="store_true", help='Get all dates (use only with api_key)')
    parser.add_argument('--get-images', default=False,
                        action="store_true", help='Get all images (required: date, api_key)')
    parser.add_argument('--get-image-url', default=False,
                        action="store_true", help='Get all images (required: date, image-id, api_key)')
    parser.add_argument('--date', default=None, type=str, help='Date to download')
    parser.add_argument('--image-id', default=None, type=str, help='Image id to download')
    parser.add_argument('--api-key', type=str, help='NASA Api Key', required=True)

    args = parser.parse_args()

    no_flags = False
    if not (args.get_dates or args.get_images or args.get_image_url):
        parser.print_help()
        no_flags = True
        exit(1)
    if (args.get_dates and args.get_images) or (args.get_images and args.get_image_url) or (args.get_dates and args.get_image_url):
        parser.print_help()
        print("ERROR: there is two flags specified")
        exit(1)
    if args.get_dates or no_flags:
        print(get_epic_dates(args.api_key))
    elif args.get_images:
        if args.date == None:
            parser.print_help()
            print("ERROR: --date is required for --get-images")
            exit(1)
        print(get_epic_image_ids(args.api_key, args.date))
    elif args.get_image_url:
        if args.date == None or args.image_id == None:
            parser.print_help()
            print("ERROR: --date and --image_id is required for --get-images")
            exit(1)
        print(build_url(get_epic_image_url(args.api_key, args.date, args.image_id)))
if __name__ == '__main__':
    main()