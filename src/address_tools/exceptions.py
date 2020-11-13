class ResolveCoordinatesError(Exception):
    pass


class NotInBrooklynError(ResolveCoordinatesError):
    def __init__(self, address, coordinates):
        self.address = address
        self.coordinates = coordinates

    def __str__(self):  
        return f'The address {self.address} has been resolved to {self.coordinates} but this is not in Brooklyn.'


class CacheMiss(Exception):
    pass
