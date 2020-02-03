from . import BasicType


class File(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'file_path': str,
        'file_size': int
    }

    def __init__(self, obj=None):
        super(File, self).__init__(obj)

    def get_file_id(self) -> str:
        return getattr(self, 'file_id', None)

    def get_file_unique_id(self) -> str:
        return getattr(self, 'file_unique_id', None)
