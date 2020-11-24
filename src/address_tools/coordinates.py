import math
from dataclasses import dataclass

from shapely.geometry.point import Point


@dataclass
class Coordinates:
    lon: float = float("NaN")
    lat: float = float("NaN")

    @staticmethod
    def from_json(value: dict):
        return Coordinates(value['lon'], value['lat'])

    def is_valid(self):
        return not math.isnan(self.lon) and not math.isnan(self.lat)

    def to_point(self):
        return Point(self.lon, self.lat)

    def to_json(self): 
        return {
            'lon': self.lon,
            'lat': self.lat
        }

    def __str__(self):
        return f'[Coordinates] {self.lon}/{self.lat}'
