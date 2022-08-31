import os
import requests
import argparse

from download import download_image

def get_flight(flight_id):
    response = requests.get("https://api.spacexdata.com/v5/launches/{}".format(flight_id))
    response.raise_for_status()
    return response.json()

def get_flight_images(flight):
    return flight["links"]["flickr"]["original"]

def main():
    parser = argparse.ArgumentParser(
        description='Tool for downloading SpaceX flight images.')
    parser.add_argument('--flight-id', type=str, 
                        help='SpaceX flight id', default="5eb87d47ffd86e000604b38a")
    parser.add_argument('--raw-json', default=False,
                        action="store_true", help='Get raw flight data')
    parser.add_argument('--no-download', default=False,
                        action="store_true", help='Do not download photos')
    
    args = parser.parse_args()

    flight_json = get_flight(args.flight_id)
    flight_images = get_flight_images(flight_json)
    if args.raw_json:
        print(flight_json)
    else:
        print(flight_images)
    
    if not args.no_download:
        for index, url in enumerate(flight_images):
            extention = os.path.splitext(url)[1]
            os.makedirs("images", exist_ok=True)
            download_image(url, os.path.join("images", f"spacex-{index}{extention}"))

if __name__ == "__main__":
    main()