import mbta.controller as api
from django.http import HttpResponse
from django.shortcuts import render
from ride.secure import secure_settings
from ride.settings import ENV
from geopy.distance import geodesic, great_circle
from mbta.utils import findMiddle, findMiddleOfCoords, getRadius
import json 

# CR-Fairmount
# CR-Fitchburg
# CR-Foxboro
# CR-Franklin
# CR-Greenbush
# CR-Haverhill
# CR-Kingston
# CR-Lowell
# CR-Middleborough
# CR-Needham
# CR-Newburyport
# CR-Providence
# CR-Worcester


def home(request):
    
    routes = api.get_routes()
    return render(request,
        'mbta/index.html',
        {
            'title': 'MBTA',
            'routes': routes,
        }
    )

def detail(request, route_id):
    route = api.get_routes(route_id)
    stops = api.get_stops(route_id)
    vehicles = api.get_vehicles(route_id)

    stop_coords = []

    for stop in stops["data"]:
        coord = ( stop["attributes"]["latitude"], stop["attributes"]["longitude"] )
        stop_coords.append(coord)
    
    center_coord = findMiddleOfCoords(stop_coords)
    lat, long = center_coord
    map_center = { "latitude" : lat, "longitude" : long }
    distance = great_circle(stop_coords[0], stop_coords[-1]).miles
    radius = getRadius(stop_coords, center_coord)

    print("Distance: {}".format(distance))
    print("Radius: {}".format(radius))
    print("Diameter: {}".format(radius*2))

    if distance <= 1:
        zoom_level = 13
    elif distance <= 3:
        zoom_level = 14
    elif distance > 3 and distance <= 5:
        zoom_level = 13
    elif distance > 5 and distance <= 10:
        zoom_level = 12
    elif distance > 10 and distance <= 30:
        zoom_level = 10
    elif distance > 30 and distance <= 50:
        zoom_level = 10
    elif distance > 50:
        zoom_level = 9
    

    return render(request,
        'mbta/detail.html',
        {
            'title': route_id,
            'route': route,
            'vehicles': vehicles,
            'stops' : stops,
            'mapkey': secure_settings["MAP_KEY"],
            'env' : ENV,
            'map_center' : map_center,
            'zoom_level' : zoom_level
        }
    )
