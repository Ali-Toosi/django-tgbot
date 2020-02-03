from typing import Optional

from . import BasicType


class LoginUrl(BasicType):
    fields = {
        'url': str,
        'forward_text': str,
        'bot_username': str,
        'request_write_access': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(LoginUrl, self).__init__(obj)

    @classmethod
    def a(cls, url: str, forward_text: Optional[str] = None, bot_username: Optional[str] = None, request_write_access: Optional[bool] = None):
        return super().a(**locals())