from typing import Optional

from . import BasicType


class ReplyKeyboardRemove(BasicType):
    fields = {
        'remove_keyboard': BasicType.bool_interpreter,
        'selective': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(ReplyKeyboardRemove, self).__init__(obj)

    @classmethod
    def a(cls, remove_keyboard: bool, selective: Optional[bool] = None):
        return super().a(**locals())
