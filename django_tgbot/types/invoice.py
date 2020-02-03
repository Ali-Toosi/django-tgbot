from . import BasicType


class Invoice(BasicType):
    fields = {
        'title': str,
        'description': str,
        'start_parameter': str,
        'currency': str,
        'total_amount': int
    }

    def __init__(self, obj=None):
        super(Invoice, self).__init__(obj)

    def get_title(self) -> str:
        return getattr(self, 'title', None)

    def get_start_parameter(self) -> str:
        return getattr(self, 'start_parameter', None)

    def get_currency(self) -> str:
        return getattr(self, 'currency', None)

    def total_amount(self) -> int:
        return getattr(self, 'total_amount', None)

    @classmethod
    def a(cls, title: str, description: str, start_parameter: str, currency: str, total_amount: int):
        return super().a(**locals())
