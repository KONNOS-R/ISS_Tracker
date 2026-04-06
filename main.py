import requests
import time


api = "http://api.open-notify.org/iss-now.json"

run = True

def getData():
    try:
        raw_data = (requests.get(api, timeout = 5)).json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    lat = raw_data["iss_position"]["latitude"]
    lon = raw_data["iss_position"]["longitude"]

    return (lat, lon)



while run:
        data = getData()
        if data != None:
            lat, lon = data
        print(f"------ISS position------\nLatitude: {lat}\nLongitude: {lon}\n")