from typing import Optional

from . import BasicType


class ChatPermissions(BasicType):
    fields = {
        'can_send_messages': BasicType.bool_interpreter,
        'can_send_media_messages': BasicType.bool_interpreter,
        'can_send_polls': BasicType.bool_interpreter,
        'can_send_other_messages': BasicType.bool_interpreter,
        'can_add_web_page_previews': BasicType.bool_interpreter,
        'can_change_info': BasicType.bool_interpreter,
        'can_invite_users': BasicType.bool_interpreter,
        'can_pin_messages': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(ChatPermissions, self).__init__(obj)

    @classmethod
    def a(cls, can_send_messages: Optional[bool] = None, can_send_media_messages: Optional[bool] = None,
          can_send_polls: Optional[bool] = None, can_send_other_messages: Optional[bool] = None,
          can_add_web_page_previews: Optional[bool] = None, can_change_info: Optional[bool] = None,
          can_invite_users: Optional[bool] = None, can_pin_messages: Optional[bool] = None):
        return super().a(**locals())

