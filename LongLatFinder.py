from distutils.log import debug
import math
import re
class locPoint:
        bearing = 74
        distance = 124800
        lon = math.radians(43)
        lat = math.radians(26)
        R = 6371000
        angularD = round(distance / R, 6)
class secondLocPoint:
    def __init__(self, lat, lon, bearing) -> None:
        self.lat = lat
        self.lon = lon
        self.bearing = bearing

def latlonDecimalConverter(loc):
    lex = loc
    deg, minutes, seconds, direction =  re.split('[°\'"]', lex) 
    newLat = (float(deg) + float(minutes) / 60 + float(seconds) / 3600) * (-1 if direction in ['W', 'S'] else 1)
    return round(newLat, 6)
def toDegree(var):
    split_degx = math.modf(var)
    
    # the whole number [index 1] is the degrees
    degrees_x = int(split_degx[1])

    # multiply the decimal part by 60: 0.3478 * 60 = 20.868
    # split the whole number part of the total as the minutes: 20
    # abs() absoulte value - no negative
    minutes_x = abs(int(math.modf(split_degx[0] * 60)[1]))

    seconds_x = abs(round(math.modf(split_degx[0] * 60)[0] * 60,2))

    return str(abs(degrees_x)) + u"\u00b0" + str(minutes_x) + "'" + str(seconds_x)

def latlonDegreeConverter(longitude, latitude):

    # math.modf() splits whole number and decimal into tuple
    split_degx = math.modf(longitude)
    
    # the whole number [index 1] is the degrees
    degrees_x = int(split_degx[1])

    # split the whole number part of the total as the minutes: 20
    # abs() absoulte value - no negative
    minutes_x = abs(int(math.modf(split_degx[0] * 60)[1]))

    # multiply the decimal part of the split above by 60 to get the seconds
    # abs() absoulte value - no negative
    seconds_x = abs(round(math.modf(split_degx[0] * 60)[0] * 60,2))

    # repeat for latitude
    split_degy = math.modf(latitude)
    degrees_y = int(split_degy[1])
    minutes_y = abs(int(math.modf(split_degy[0] * 60)[1]))
    seconds_y = abs(round(math.modf(split_degy[0] * 60)[0] * 60,2))

    # account for E/W & N/S
    if degrees_x < 0:
        EorW = "W"
    else:
        EorW = "E"

    if degrees_y < 0:
        NorS = "S"
    else:
        NorS = "N"

    # abs() remove negative from degrees, was only needed for if-else above
    print(str(abs(degrees_x)) + u"\u00b0" + str(minutes_x) + "'" + str(seconds_x) + "\"" + EorW)
    print(str(abs(degrees_y)) + u"\u00b0" + str(minutes_y) + "'" + str(seconds_y) + "\"" + NorS)

def distanceBearing():
    lat2 = math.asin(math.sin(locPoint.lat) * math.cos(locPoint.angularD) + 
    math.cos(locPoint.lat) * math.sin(locPoint.angularD) * math.cos(locPoint.bearing))

    lon2 = locPoint.lon + math.atan2(math.sin(locPoint.bearing) * math.sin(locPoint.angularD)
     * math.cos(locPoint.lat), math.cos(locPoint.angularD) - math.sin(locPoint.lat) * math.sin(lat2))

    dlon = locPoint.lon - lon2
    y = math.sin(dlon) * math.cos(locPoint.lat)
    x = math.cos(lat2) * math.sin(locPoint.lat) - math.sin(lat2) * math.cos(locPoint.lat) * math.cos(dlon)
    z = math.atan2(y,x)
    finalBearing = toDegree(math.degrees(z + math.pi))
    
    result = secondLocPoint(round(math.degrees(lat2), 6),  round(math.degrees(lon2), 6), finalBearing)
    return result

locPoint.lat = math.radians(latlonDecimalConverter('''53°19'14"N'''))
locPoint.lon = math.radians(latlonDecimalConverter('''001°43'47"W'''))
locPoint.bearing = math.radians(latlonDecimalConverter('''096°01'18"'''))

object = distanceBearing()
print( "Latitude:", object.lat, " Longitude:", object.lon, " FinalBearing:", object.bearing)