from . import BasicType


class PassportFile(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'file_size': int,
        'file_date': int
    }

    def __init__(self, obj=None):
        super(PassportFile, self).__init__(obj)
