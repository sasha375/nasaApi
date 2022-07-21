import datetime
import requests

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