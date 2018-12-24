# put utility functions here

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return [input_list[int(middle - .5)]]
    else:
        return [input_list[int(middle)], input_list[int(middle-1)]]

def findMiddleOfCoords( point1, point2):
    lat1, long1 = point1
    lat2, long2 = point2

    new_lat = lat1 + lat2
    new_long = long1 + long2

    return (new_lat/2, new_long/2)