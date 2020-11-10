from address_tools.exceptions import CacheMiss, ResolveCoordinatesError
import requests

from address_tools.coordinates import Coordinates

from address_tools.coordinates import Coordinates
from address_tools.cache import address_cache


def get_coordinates_from_address(address: str, resolve=False) -> Coordinates:
    """Resolve the adress to coordiantes asling the nominatim service from openstreetmap.org

        return (dict) Returns a dict with lon and lat entries. In case of error the lon/lat contains NaN
    """
    try:
        coordinates = address_cache[address]
        if resolve and not coordinates.is_valid():
            raise CacheMiss()
        return coordinates
    except CacheMiss:
        try:
            coordinates = _resolve_address(address)
        except ResolveCoordinatesError as e:
            coordinates = {
                'lon': float("NaN"),
                'lat': float("NaN")
            }
        address_cache[address] = coordinates
        return coordinates



class BaseAddressResolver:

    def resolve(self, address) -> Coordinates:
        raise NotImplemented()


class OpenStreetMapResolver(BaseAddressResolver):

    NOMINATIM_URL = 'https://nominatim.openstreetmap.org/search.php'


    def resolve(self, address: str) -> Coordinates:
        params = {
                'street': address, 
                'county': 'Brooklyn',
                'polygon_geojson': 1,
                'format': 'jsonv2',
                }
        try:
            response = requests.post(self.NOMINATIM_URL, params=params)
            response.raise_for_status()
            box = response.json()[0]

            return Coordinates(float(box['lon']), float(box['lat']))
            
        except Exception as e:
            raise ResolveCoordinatesError(f'Failed to get address from openstreetmap: {address}, reason: {e}')

class GoogleAddressResolver(BaseAddressResolver):
    API_KEY = 'INSERT YOUR KEY HERE'
    GOOGLE_GEOAPI_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

    def resolve(self, address: str) -> Coordinates:
        params = {
            'address': f"{address}, Brooklyn",
            'key': self.API_KEY
        }

        response = requests.post(self.GOOGLE_GEOAPI_URL, params=params)
        try:
            response.raise_for_status()

            r_data = response.json()
            location = r_data['results'][0]['geometry']['location']
            return Coordinates(location['lng'], location['lat'])

        except Exception as e:
            raise ResolveCoordinatesError(f'Failed to get coordinates from google API: {address}, reason: {e}')

def _resolve_address(address: str):
        print(f'Resolve: {address}')
        for cls in (OpenStreetMapResolver, GoogleAddressResolver):
            try:
                print(f'  ask {cls.__name__}')
                return cls().resolve(address)
            except ResolveCoordinatesError as e:
                print(f'  ERROR: {e}')

        return Coordinates()