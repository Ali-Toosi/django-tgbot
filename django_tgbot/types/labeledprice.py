from . import BasicType


class LabeledPrice(BasicType):
    fields = {
        'label': str,
        'amount': int
    }

    def __init__(self, obj=None):
        super(LabeledPrice, self).__init__(obj)

    def get_label(self) -> str:
        return getattr(self, 'label', None)

    def get_amount(self) -> int:
        return getattr(self, 'amount', None)

    @classmethod
    def a(cls, label: str, amount: int):
        return super().a(**locals())