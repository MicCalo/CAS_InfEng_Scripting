import json
from functools import cached_property
from shapely.geometry.polygon import Polygon

from address_tools.coordinates import Coordinates


class Brooklyn:

    @cached_property
    def brooklyn_polygon(self):
        return self._load_brooklyn_polygon()

    @property
    def center(self):
        return self.brooklyn_polygon.centroid

    def contains(self, coordinates: Coordinates):
        return self.brooklyn_polygon.contains(coordinates.to_point())

    def _load_brooklyn_polygon(self):
        with open('./../data/2_intermediate/brooklyn_border.geojson') as file:
            data = json.load(file)
            return Polygon(data['geometry']['coordinates'][0])

