
import math
import re
class locPoint:
        bearing = 74
        distance = 124800
        lon = 43
        lat = 26
        R = 6371000
        angularD = round(distance / R, 6)

def latlonDecimalConverter(loc):
    lex = loc
    deg, minutes, seconds, direction =  re.split('[°\'"]', lex) 
    newLat = (float(deg) + float(minutes) / 60 + float(seconds) / 3600) * (-1 if direction in ['W', 'S'] else 1)
    return round(newLat, 6)

def kes():
    lat2 = math.asin(math.sin(locPoint.lat) * math.cos(locPoint.angularD) + 
    math.cos(locPoint.lat) * math.sin(locPoint.angularD) * math.cos(locPoint.bearing))

    lon2 = locPoint.lon + math.atan2(math.sin(locPoint.bearing) * math.sin(locPoint.angularD)
     * math.cos(locPoint.lat), math.cos(locPoint.angularD) - math.sin(locPoint.lat) * math.sin(lat2))

    print(lat2, ", ", lon2)

locPoint.lat = math.radians(latlonDecimalConverter('''53°19'14"N'''))
locPoint.lon = math.radians(latlonDecimalConverter('''001°43'47"W'''))
locPoint.bearing = math.radians(latlonDecimalConverter('''096°01'18"'''))

kes()
print(locPoint.lat, locPoint.lon, locPoint.bearing, locPoint.angularD)