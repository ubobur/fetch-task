import argparse
import requests # type: ignore
from typing import List, Dict

API_KEY = "f897a99d971b5eef57be6fafa0d83239"
BASE_URL = "http://api.openweathermap.org/geo/1.0/"

def get_location_by_name(location: str) -> Dict:
    url = f"{BASE_URL}direct?q={location},US&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data:
        return {
            "name": data[0]["name"],
            "state": data[0]["state"],
            "country": data[0]["country"],
            "lat": data[0]["lat"],
            "lon": data[0]["lon"]
        }
    return {}

def get_location_by_zip(zipcode: str) -> Dict:
    url = f"{BASE_URL}zip?zip={zipcode},US&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if "name" in data:
        return {
            "name": data["name"],
            "country": data["country"],
            "lat": data["lat"],
            "lon": data["lon"],
            "zip": zipcode
        }
    return {}

def get_location_info(location: str) -> Dict:
    if location.replace(",", "").replace(" ", "").isdigit():
        return get_location_by_zip(location)
    else:
        return get_location_by_name(location)

def main(locations: List[str]):
    for location in locations:
        info = get_location_info(location)
        if info:
            print(f"Location: {location}")
            for key, value in info.items():
                print(f"{key.capitalize()}: {value}")
            print()
        else:
            print(f"No information found for location: {location}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Geocoding utility for US locations")
    parser.add_argument("locations", nargs="+", help="List of locations (city, state or zip code)")
    args = parser.parse_args()
    main(args.locations)
