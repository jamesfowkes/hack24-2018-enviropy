from geopy.distance import vincenty

from collections import namedtuple

class LatLng(namedtuple("LatLng", ["lat", "lng"])):
    __slots__ = ()

    def distance_from(self, other, miles=False):
        return vincenty(self, other).miles if miles else vincenty(self, other).km

    @classmethod 
    def from_string(cls, s):
        parts = s.split(",")
        lat = float(parts[0].strip())
        lng = float(parts[1].strip())
        return cls(lat, lng)

    @classmethod
    def from_midpoint(cls, p1, p2):
        lat = (p1.lat+p2.lat) / 2
        lng = (p1.lng+p2.lng) / 2
        return cls(lat, lng)