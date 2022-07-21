import requests
import argparse

def get_flight(flight_id):
    response = requests.get("https://api.spacexdata.com/v5/launches/{}".format(flight_id))
    response.raise_for_status()
    return response.json()

def get_flight_images(flight_id):
    flight = get_flight(flight_id)
    return flight["links"]["flickr"]["original"]