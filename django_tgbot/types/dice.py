from . import BasicType


class Dice(BasicType):
    fields = {
        'emoji': str,
        'value': int
    }

    def __init__(self, obj=None):
        super(Dice, self).__init__(obj)

    def get_emoji(self) -> str:
        return getattr(self, 'emoji')

    def get_value(self) -> int:
        return getattr(self, 'value')

    @classmethod
    def a(cls, emoji: str, value: int):
        return super().a(**locals())
