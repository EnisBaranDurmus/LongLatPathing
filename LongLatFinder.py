
import math
import re
class locPoint:
        bearing = 74
        distance = 124800
        lon = 43
        lat = 26
        R = 6371
        angularD = distance / R

def latlonDecimalConverter(loc):
    lat = loc
    deg, minutes, seconds, direction =  re.split('[°\'"]', lat) 
    newLat = float(deg) + float(minutes) / 60 + float(seconds) / 3600 * (-1 if direction in ['W', 'S'] else 1)
    round(newLat,6)

def kes():
    lat2 = math.asin(math.sin(locPoint.lat) * math.cos(locPoint.bearing) + math.cos(locPoint.lat) * math.sin(locPoint.angularD) * math.cos(locPoint.bearing))
    lon2 = locPoint.lon + math.atan2(math.sin(locPoint.bearing) * math.sin(locPoint.angularD) * math.cos(locPoint.lat), math.cos(locPoint.angularD) - math.sin(locPoint.lat) * math.sin(lat2))
    print(lat2, ", ", lon2)

kes()