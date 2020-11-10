from address_tools.exceptions import CacheMiss
import json

from address_tools.coordinates import Coordinates


class AddressCache:

    CACHE_FILE = 'address_cache.json'

    def __init__(self):
        self.cache = self._read_from_file()

    def write_to_file(self):
        with open(self.CACHE_FILE, 'w') as fp:
            return json.dump(self.cache, fp)

    def _read_from_file(self):
        try:
            with open(self.CACHE_FILE) as fp:
                return json.load(fp)
        except FileNotFoundError:
            return {}
    
    def __getitem__(self, key: str):
        try:
            return Coordinates.from_json(self.cache[key])
        except KeyError:
            raise CacheMiss(f'Cache does not contain "{key}"')

    def __setitem__(self, key: str, value: Coordinates):
        self.cache[key] = value.to_json()
        self.write_to_file()


address_cache = AddressCache()
