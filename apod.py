import requests
import argparse

def get_apod_urls(api_key, count):
    response = requests.get("https://api.nasa.gov/planetary/apod",
                            params={"api_key": api_key, "count": count})
    response.raise_for_status()
    return [apod["url"] for apod in response.json()]