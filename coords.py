import math

# A class that represents a point in Earth
class Coords:
    latitude  = None
    longitude = None

    # Constructor, requires lat and long in degrees.
    # Angles are converted to radians right away.
    def __init__(self, lat, lon):
        self.latitude  = math.radians(lat)
        self.longitude = math.radians(lon)

    # Calculates the distance between two points
    # May contain rounding errors in systems using 32bit floats
    def distance(self, other):
        # Absolute difference of longitudes
        d_long = abs(self.longitude - other.longitude)

        # The angle between the two points, according to the 
        # grand-circle distance formula
        angle = math.acos(
            math.sin(self.latitude) * math.sin(other.latitude) +
            math.cos(self.latitude) * math.cos(other.latitude) * math.cos(d_long)
        )

        # Distance is given by multiplying the angle (in radians) by the radius 
        # of the sphere (mean radius of Earth).
        return 6371.009 * angle

