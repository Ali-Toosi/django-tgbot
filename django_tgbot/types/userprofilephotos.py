from . import BasicType


class UserProfilePhotos(BasicType):
    fields = {
        'total_count': int,
    }

    def __init__(self, obj=None):
        super(UserProfilePhotos, self).__init__(obj)


from . import photosize

UserProfilePhotos.fields.update({
    'photos': {
        'class': photosize.PhotoSize,
        'array_of_array': True
    }
})