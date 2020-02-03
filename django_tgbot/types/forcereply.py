from typing import Optional

from . import BasicType


class ForceReply(BasicType):
    fields = {
        'force_reply': BasicType.bool_interpreter,
        'selective': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(ForceReply, self).__init__(obj)

    @classmethod
    def a(cls, force_reply: bool, selective: Optional[bool] = None):
        return super().a(**locals())
