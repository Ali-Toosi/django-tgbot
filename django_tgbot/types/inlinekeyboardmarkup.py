from typing import List

from . import BasicType
from . import inlinekeyboardbutton


class InlineKeyboardMarkup(BasicType):
    fields = {
        'inline_keyboard': {
            'class': inlinekeyboardbutton.InlineKeyboardButton,
            'array_of_array': True
        }
    }

    def __init__(self, obj=None):
        super(InlineKeyboardMarkup, self).__init__(obj)

    @classmethod
    def a(cls, inline_keyboard: List[List[inlinekeyboardbutton.InlineKeyboardButton]]):
        return super().a(**locals())
