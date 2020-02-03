from . import BasicType
from . import photosize, maskposition


class Sticker(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'width': int,
        'height': int,
        'is_animated': BasicType.bool_interpreter,
        'thumb': photosize.PhotoSize,
        'emoji': str,
        'set_name': str,
        'mask_position': maskposition.MaskPosition,
        'file_size': int
    }

    def __init__(self, obj=None):
        super(Sticker, self).__init__(obj)

