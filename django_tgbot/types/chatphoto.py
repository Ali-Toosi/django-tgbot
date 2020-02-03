from . import BasicType


class ChatPhoto(BasicType):
    fields = {
        'small_file_id': str,
        'small_file_unique_id': str,
        'big_file_id': str,
        'big_file_unique_id': str
    }

    def __init__(self, obj=None):
        super(ChatPhoto, self).__init__(obj)