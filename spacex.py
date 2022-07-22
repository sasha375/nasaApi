import requests
import argparse

def get_flight(flight_id):
    response = requests.get("https://api.spacexdata.com/v5/launches/{}".format(flight_id))
    response.raise_for_status()
    return response.json()

def get_flight_images(flight_id):
    flight = get_flight(flight_id)
    return flight["links"]["flickr"]["original"]

def main():
    parser = argparse.ArgumentParser(
        description='Tool for downloading SpaceX flight images.')
    parser.add_argument('--flight-id', type=str, 
                        help='SpaceX flight id', required=True)
    parser.add_argument('--raw-json', default=False,
                        action="store_true", help='Get raw flight data')
    
    args = parser.parse_args()

    if args.raw_json:
        print(get_flight(args.flight_id))
    else:
        print(get_flight_images(args.flight_id))

if __name__ == "__main__":
    main()