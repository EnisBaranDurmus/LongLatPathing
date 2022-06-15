
import math
lat = math.radians(31)
lon = math.radians(31)
R = 6371
bearing = math.radians(0)
distance = 100
angularD = distance / R

def distanceBearing():
    lat2 = math.asin(math.sin(lat) * math.cos(angularD) + 
    math.cos(lat) * math.sin(angularD) * math.cos(bearing))

    lon2 = lon + math.atan2(math.sin(bearing) * math.sin(angularD)
     * math.cos(lat), math.cos(angularD) - math.sin(lat) * math.sin(lat2))

    dlon = lon - lon2
    y = math.sin(dlon) * math.cos(lat)
    x = math.cos(lat2) * math.sin(lat) - math.sin(lat2) * math.cos(lat) * math.cos(dlon)
    z = math.atan2(y,x)
    
    print(round(math.degrees(lat2), 6),  round(math.degrees(lon2), 6))

distanceBearing()