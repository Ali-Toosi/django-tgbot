from . import BasicType
from . import orderinfo


class SuccessfulPayment(BasicType):
    fields = {
        'currency': str,
        'total_amount': int,
        'invoice_payload': str,
        'shipping_option_id': str,
        'order_info': orderinfo.OrderInfo,
        'telegram_payment_charge_id': str,
        'provider_payment_charge_id': str,
    }

    def __init__(self, obj=None):
        super(SuccessfulPayment, self).__init__(obj)