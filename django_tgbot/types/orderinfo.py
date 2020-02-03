from typing import Optional

from . import BasicType


class OrderInfo(BasicType):
    fields = {
        'name': str,
        'phone_number': str,
        'email': str,
    }

    def __init__(self, obj=None):
        super(OrderInfo, self).__init__(obj)

    def get_name(self) -> Optional[str]:
        return getattr(self, 'name', None)

    def get_shipping_address(self):  # -> Optional[shippingaddress.ShippingAddress]:
        return getattr(self, 'shipping_address')


from . import shippingaddress

OrderInfo.fields.update({
    'shipping_address': shippingaddress.ShippingAddress
})