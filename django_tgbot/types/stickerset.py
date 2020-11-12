from . import BasicType
from . import sticker, photosize


class StickerSet(BasicType):
    fields = {
        'name': str,
        'title': str,
        'is_animated': BasicType.bool_interpreter,
        'contains_masks': BasicType.bool_interpreter,
        'stickers': {
            'class': sticker.Sticker,
            'array': True
        },
        'thumb': photosize.PhotoSize
    }

    def __init__(self, obj=None):
        super(StickerSet, self).__init__(obj)
