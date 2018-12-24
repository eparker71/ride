import mbta.controller as api
from django.http import HttpResponse
from django.shortcuts import render
from ride.secure import secure_settings
from ride.settings import ENV

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

    return render(request,
        'mbta/detail.html',
        {
            'title': route_id,
            'route': route,
            'vehicles': vehicles,
            'stops' : stops,
            'mapkey': secure_settings["MAP_KEY"],
            'env' : ENV
        }
    )
