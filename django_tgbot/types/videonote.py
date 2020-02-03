from . import BasicType
from . import photosize


class VideoNote(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'length': int,
        'duration': int,
        'file_size': int,
        'thumb': photosize.PhotoSize
    }

    def __init__(self, obj=None):
        super(VideoNote, self).__init__(obj)
