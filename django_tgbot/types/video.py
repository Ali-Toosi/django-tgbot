from . import BasicType


class Video(BasicType):
    fields = {
        'file_id': str,
        'file_unique_id': str,
        'width': int,
        'height': int,
        'duration': int,
        'mime_type': str,
        'file_size': int,
    }

    def __init__(self, obj=None):
        super(Video, self).__init__(obj)


from . import photosize

Video.fields.update({
    'thumb': photosize.PhotoSize
})