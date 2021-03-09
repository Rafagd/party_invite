import coords
import customers
import math
import random

# Test if coods are being created and if their
# lats/lons are in radians after creation
def test_coords():
    for i in range(1000):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        cds = coords.Coords(lat, lon)
        assert cds.latitude  == math.radians(lat)
        assert cds.longitude == math.radians(lon)

# Tests if we have a couple of known distances
# Also tests if the distance is the same on the oposite direction
def test_distance():
    c1 = coords.Coords(0, 0)
    
    c2 = coords.Coords(0,  90)
    c3 = coords.Coords(0, -90)
    assert int(c1.distance(c2)) == 10007
    assert int(c2.distance(c1)) == 10007
    assert int(c1.distance(c3)) == 10007
    assert int(c3.distance(c1)) == 10007

    c2 = coords.Coords(0,  180)
    c3 = coords.Coords(0, -180)
    assert int(c1.distance(c2)) == 20015
    assert int(c2.distance(c1)) == 20015
    assert int(c1.distance(c3)) == 20015
    assert int(c3.distance(c1)) == 20015

def test_customer():
    auid  = int(random.uniform(0, 1000))
    alat  = random.uniform(-90, 90)
    along = random.uniform(-180, 180)
    alice = customers.Customer(auid, 'Alice', coords.Coords(alat, along))

    assert alice.user_id == auid
    assert alice.name    == 'Alice'
    assert alice.coords.latitude  == math.radians(alat)
    assert alice.coords.longitude == math.radians(along)


