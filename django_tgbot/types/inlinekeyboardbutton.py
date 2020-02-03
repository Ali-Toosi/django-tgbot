from typing import Optional

from . import BasicType
from . import loginurl


class InlineKeyboardButton(BasicType):
    fields = {
        'text': str,
        'url': str,
        'login_url': loginurl.LoginUrl,
        'callback_data': str,
        'switch_inline_query': str,
        'switch_inline_query_current_chat': str,
        'callback_game': str,
        'pay': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(InlineKeyboardButton, self).__init__(obj)

    @classmethod
    def a(cls, text: str, url: Optional[str] = None, login_url: Optional[loginurl.LoginUrl] = None,
          callback_data: Optional[str] = None, switch_inline_query: Optional[str] = None,
          switch_inline_query_current_chat: Optional[str] = None, callback_game: Optional[str] = None,
          pay: Optional[bool] = None):
        return super().a(**locals())
