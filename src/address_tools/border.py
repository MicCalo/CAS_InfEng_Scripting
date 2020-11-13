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

    def contains(self, coordiantes: Coordinates):
        return self.brooklyn_polygon.contains(coordiantes.to_point())

    def _load_brooklyn_polygon(self):
        with open('./../data/intermediate/brooklyn_border.json') as file:
            data = json.load(file)
            return Polygon(data['coordinates'][0])

