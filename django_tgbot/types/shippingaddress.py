from . import BasicType


class ShippingAddress(BasicType):
    fields = {
        'country_code': str,
        'state': str,
        'city': str,
        'street_line1': str,
        'street_line2': str,
        'post_code': str
    }

    def __init__(self, obj=None):
        super(ShippingAddress, self).__init__(obj)

