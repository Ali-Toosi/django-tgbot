from typing import Optional

from . import BasicType
from . import keyboardbuttonpolltype


class KeyboardButton(BasicType):
    fields = {
        'text': str,
        'request_contact': BasicType.bool_interpreter,
        'request_location': BasicType.bool_interpreter,
        'request_poll': keyboardbuttonpolltype.KeyboardButtonPollType
    }

    def __init__(self, obj=None):
        super(KeyboardButton, self).__init__(obj)

    @classmethod
    def a(cls, text: str, request_contact: Optional[bool] = None, request_location: Optional[bool] = None,
          request_poll: Optional[keyboardbuttonpolltype.KeyboardButtonPollType] = None):
        return super().a(**locals())
