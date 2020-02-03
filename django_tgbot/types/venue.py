from . import BasicType


class Venue(BasicType):
    fields = {
        'title': str,
        'address': str,
        'foursquare_id': str,
        'foursquare_type': str,
    }

    def __init__(self, obj=None):
        super(Venue, self).__init__(obj)


from . import location

Venue.fields.update({
    'location': location.Location
})