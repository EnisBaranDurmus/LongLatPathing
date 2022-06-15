from rep import LongLatFinder as loc
import math
loc.locPoint.lat = math.radians(31)
loc.locPoint.lon = math.radians(31)
loc.locPoint.distance = 100
loc.locPoint.R = 6371
loc.locPoint.bearing = 0
loc.locPoint.angularD = 100 / 6371
object = loc.distanceBearing()
print( "Latitude:", object.lat, " Longitude:", object.lon, " FinalBearing:", object.bearing)
