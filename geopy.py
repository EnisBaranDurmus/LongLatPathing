import geopy.distance
# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
origin = geopy.Point(53.320556, -1.729722)
geopy.distance.distance(kilometers=124.8).destination((53.320556, -1.729722),96.021667)
