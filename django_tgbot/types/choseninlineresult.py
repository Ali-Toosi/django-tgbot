from typing import Optional

from . import BasicType


class ChosenInlineResult(BasicType):
    fields = {
        'result_id': str,
        'inline_message_id': str,
        'query': str
    }

    def __init__(self, obj=None):
        super(ChosenInlineResult, self).__init__(obj)

    def get_user(self):  # -> user.User:
        return getattr(self, 'from', None)

    def get_from(self):
        return self.get_user()

    def get_result_id(self) -> str:
        return getattr(self, 'result_id', None)

    def get_inline_message_id(self):  # -> Optional[str]
        return getattr(self, 'inline_message_id', None)

    def get_query(self) -> str:
        return getattr(self, 'query', None)

    def get_location(self):  # -> Optional[location.Location]
        return getattr(self, 'location', None)


# Placed here to avoid import cycles
from . import user, location

ChosenInlineResult.fields.update({
    'from': user.User,
    'location': location.Location,
})
