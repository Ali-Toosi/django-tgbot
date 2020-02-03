from . import BasicType


class Animation(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'width': int,
        'height': int,
        'duration': int,
        'file_name': str,
        'mime_type': str,
        'file_size': int,
    }

    def __init__(self, obj=None):
        super(Animation, self).__init__(obj)

    def get_file_id(self):
        return getattr(self, 'file_id', None)


# Placed here to avoid import cycles

from . import photosize

Animation.fields.update({
    'thumb': photosize.PhotoSize
})
