from datetime import datetime
import os
import pytz
import requests
import json
API_URL_MAPS = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&output=json&key={}'
API_URL_MAPS_KEY= 'AIzaSyBm79E2asu6A3dxmizt8wKmVrLxSeSJyYE'
API_WEATHER_KEY = '45cc9190a571fff6eae3d64833272511'
API_WEATHER = 'http://api.openweathermap.org/data/2.5/weather?zip={}&mode=json&units=metric&appid={}'


def query_api(address):
    try:
        print(API_URL_MAPS.format(address, API_URL_MAPS_KEY))
        datafrommaps = requests.get(API_URL_MAPS.format(address, API_URL_MAPS_KEY)).json()
        # print(datafrommaps)
        # datafiltered = json.loads(datafrommaps)
        # print(datafiltered)
        print(API_WEATHER.format(address, API_WEATHER_KEY))
        data = requests.get(API_WEATHER.format(address, API_WEATHER_KEY)).json()
    except Exception as exc:
        data = None
    return data