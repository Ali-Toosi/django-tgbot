from typing import Optional

from . import BasicType


class KeyboardButtonPollType(BasicType):
    fields = {
        'type': str,
    }

    def __init__(self, obj=None):
        super(KeyboardButtonPollType, self).__init__(obj)

    @classmethod
    def a(cls, type: Optional[str] = None):
        return super().a(**locals())
