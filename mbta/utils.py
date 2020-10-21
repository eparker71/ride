# put utility functions here

from geopy.distance import geodesic, great_circle

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return [input_list[int(middle - .5)]]
    else:
        return [input_list[int(middle)], input_list[int(middle-1)]]

def findMiddleOfCoords( coords ):
    lats = []
    longs = []

    for c in coords:
        lat, long = c
        lats.append(lat)
        longs.append(long)

    sum_lat = sum(float(item) for item in lats)
    sum_long = sum(float(item) for item in longs)
    newlat = sum_lat/len(lats)
    newlong = sum_long/len(longs)

    return (newlat, newlong)

def getRadius(coords, center):

    dist_list = []
    for coord in coords:
        distance = great_circle(center, coord).miles
        dist_list.append(distance)
    
    dist_list.sort()

    return dist_list[-1]

