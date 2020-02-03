from . import BasicType


class PhotoSize(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'width': int,
        'height': int,
        'file_size': int
    }

    def __init__(self, obj=None):
        super(PhotoSize, self).__init__(obj)

    def get_file_id(self) -> str:
        return getattr(self, 'file_id', None)
