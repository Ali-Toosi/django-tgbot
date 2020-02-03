from . import BasicType


class InlineQuery(BasicType):
    fields = {
        'id': str,
        'query': str,
        'offset': str
    }

    def __init__(self, obj=None):
        super(InlineQuery, self).__init__(obj)

    def get_user(self):  # -> user.User:
        return getattr(self, 'from', None)

    def get_id(self) -> str:
        return getattr(self, 'id', None)

    def get_query(self) -> str:
        return getattr(self, 'query', None)

    def get_offset(self) -> str:
        return getattr(self, 'offset', None)


from . import user, location

InlineQuery.fields.update({
    'from': user.User,
    'location': location.Location,
})