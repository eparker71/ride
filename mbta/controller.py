import requests
import json
import pprint
from urllib.parse import urlencode
from ride.secure import secure_settings
from ride.settings import app_settings

API_KEY = secure_settings.get("API_KEY")
BASE_URL = app_settings.get("API_URL")

def get_routes(id=None):
    if(id):
        route_url = "{}/routes/{}".format(BASE_URL,id)
    else:
        route_url = "{}/routes".format(BASE_URL)
    r = requests.get(route_url, headers={'x-api-key': API_KEY})
    return r.json()

def get_route_names():
    route_list = []
    routes = get_routes()
    for route in routes["data"]:
        route_list.append(route["id"])
    return route_list

def get_vehicles(route):
    route_url = "{}vehicles".format(BASE_URL)
    params =  {'filter[route]': route}
    r = requests.get(route_url, params=params,headers={'x-api-key': API_KEY})
    return r.json()



# def get_trips(route=None):
#     route_url = "{}/trips?filter[route]={}&sort=headsign".format(BASE_URL, route)
#     r = requests.get(route_url, headers={'x-api-key': API_KEY})
#     return r.json()

# def get_vehicles(route=None):
#     route_url = "{}/vehicles?filter[route]={}&sort=bearing".format(BASE_URL, route)
#     r = requests.get(route_url, headers={'x-api-key': API_KEY})
#     return r.json()
