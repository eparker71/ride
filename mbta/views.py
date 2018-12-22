from django.shortcuts import render

import mbta.controller as api

# Create your views here.

from django.http import HttpResponse

def home(request):
    
    routes = api.get_routes()

    vehicles = api.get_vehicles('CR-Fitchburg')

    return render(request,
        'mbta/index.html',
        {
            'title': 'MBTA CR',
            'routes': routes,
            'vehicles': vehicles
        }
    )
