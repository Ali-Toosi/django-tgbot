from . import BasicType


class Document(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'file_name': str,
        'mime_type': str,
        'file_size': int
    }

    def __init__(self, obj=None):
        super(Document, self).__init__(obj)

    def get_file_id(self) -> str:
        return getattr(self, 'file_id', None)


# Placed here to avoid import cycles

from . import photosize

Document.fields.update({
    'thumb': photosize.PhotoSize
})
