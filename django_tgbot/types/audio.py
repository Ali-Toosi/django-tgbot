from . import BasicType


class Audio(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'duration': int,
        'performer': str,
        'title': str,
        'mime_type': str,
        'file_size': int,
    }

    def __init__(self, obj=None):
        super(Audio, self).__init__(obj)

    def get_file_id(self):
        return getattr(self, 'file_id', None)


# Placed here to avoid import cycles

from . import photosize

Audio.fields.update({
    'thumb': photosize.PhotoSize
})
