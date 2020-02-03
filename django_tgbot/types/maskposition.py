from . import BasicType


class MaskPosition(BasicType):
    fields = {
        'point': str,
        'x_shift': str,
        'y_shift': str,
        'scale': str
    }

    def __init__(self, obj=None):
        super(MaskPosition, self).__init__(obj)

    @classmethod
    def a(cls, point: str, x_shift: str, y_shift: str, scale: str):
        return super().a(**locals())
