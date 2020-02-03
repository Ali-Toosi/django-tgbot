from . import BasicType


class PreCheckoutQuery(BasicType):
    fields = {
        'id': str,
        'currency': str,
        'total_amount': int,
        'invoice_payload': str,
        'shipping_option_id': str,
    }

    def __init__(self, obj=None):
        super(PreCheckoutQuery, self).__init__(obj)

    def get_user(self):
        return getattr(self, 'from', None)

    def get_from(self):
        return self.get_user()


from . import user, orderinfo

PreCheckoutQuery.fields.update({
    'from': user.User,
    'order_info': orderinfo.OrderInfo
})
