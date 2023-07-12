from typing import Optional

from . import BasicType


class ForceReply(BasicType):
    fields = {
        'force_reply': BasicType.bool_interpreter,
        'input_field_placeholder': str,
        'selective': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(ForceReply, self).__init__(obj)

    @classmethod
    def a(cls, force_reply: bool, input_field_placeholder: Optional[str] = None, selective: Optional[bool] = None):
        return super().a(**locals())
