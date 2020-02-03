from . import BasicType


class MessageEntity(BasicType):
    fields = {
        'type': str,
        'offset': int,
        'length': int,
        'url': str,
        'language': str,
    }

    def __init__(self, obj=None):
        super(MessageEntity, self).__init__(obj)

    def get_type(self) -> str:
        return getattr(self, 'type', None)


from . import user
MessageEntity.fields.update({
    'user': user.User
})