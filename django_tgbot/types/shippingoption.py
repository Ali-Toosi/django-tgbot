from . import BasicType
from . import labeledprice


class ShippingOption(BasicType):
    fields = {
        'id': str,
        'title': str,
        'prices': {
            'class': labeledprice.LabeledPrice,
            'array': True
        }
    }

    def __init__(self, obj=None):
        super(ShippingOption, self).__init__(obj)