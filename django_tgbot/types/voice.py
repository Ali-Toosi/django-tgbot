from . import BasicType


class Voice(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'duration': int,
        'mime_type': str,
        'file_size': int
    }

    def __init__(self, obj=None):
        super(Voice, self).__init__(obj)

