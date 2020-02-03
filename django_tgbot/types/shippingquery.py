from . import BasicType


class ShippingQuery(BasicType):
    fields = {
        'id': str,
        'invoice_payload': str
    }

    def __init__(self, obj=None):
        super(ShippingQuery, self).__init__(obj)

    def get_user(self):
        return getattr(self, 'from', None)

    def get_from(self):
        return self.get_user()


from . import user, shippingaddress

ShippingQuery.fields.update({
    'from': user.User,
    'shipping_address': shippingaddress.ShippingAddress
})