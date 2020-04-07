from typing import List, Optional

from . import BasicType
from . import keyboardbutton


class ReplyKeyboardMarkup(BasicType):
    fields = {
        'keyboard': {
            'class': keyboardbutton.KeyboardButton,
            'array_of_array': True
        },
        'resize_keyboard': BasicType.bool_interpreter,
        'one_time_keyboard': BasicType.bool_interpreter,
        'selective': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(ReplyKeyboardMarkup, self).__init__(obj)

    @classmethod
    def a(cls, keyboard: List[List[keyboardbutton.KeyboardButton]], resize_keyboard: Optional[bool] = None,
          one_time_keyboard: Optional[bool] = None, selective: Optional[bool] = None):
        return super().a(**locals())

