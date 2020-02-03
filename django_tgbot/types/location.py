from . import BasicType


class Location(BasicType):
    fields = {
        'longitude': str,
        'latitude': str
    }

    def __init__(self, obj=None):
        super(Location, self).__init__(obj)

    @classmethod
    def a(cls, latitude: str, longitude: str):
        return super().a(**locals())
