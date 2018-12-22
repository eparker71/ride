import mbta.controller as api
from django.http import HttpResponse
from django.shortcuts import render
from ride.secure import secure_settings

def home(request):
    
    routes = api.get_routes()
    stops = api.get_stops("CR-Fitchburg")
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
    vehicles = api.get_vehicles("CR-Fitchburg")

    return render(request,
        'mbta/index.html',
        {
            'title': 'MBTA CR',
            'routes': routes,
            'vehicles': vehicles,
            'stops' : stops,
            'mapkey': secure_settings["MAP_KEY"]
        }
    )
