from typing import Optional
from . import BasicType


class Chat(BasicType):
    fields = {
        'id': str,
        'type': str,
        'title': str,
        'username': str,
        'first_name': str,
        'last_name': str,
        'description': str,
        'invite_link': str,
        'slow_mode_delay': str,
        'sticker_set_name': str
    }

    def __init__(self, obj=None):
        super(Chat, self).__init__(obj)

    def get_id(self) -> str:
        return getattr(self, 'id', None)

    def get_type(self) -> str:
        return getattr(self, 'type', None)

    def get_title(self) -> Optional[str]:
        return getattr(self, 'title', None)

    def get_username(self) -> Optional[str]:
        return getattr(self, 'username', None)

    def get_first_name(self) -> Optional[str]:
        return getattr(self, 'first_name', None)

    def get_last_name(self):
        return getattr(self, 'last_name', None)

    def get_photo(self):
        return getattr(self, 'photo', None)


# These are placed here to avoid import cycles

from . import chatphoto, message, chatpermissions

Chat.fields.update({
    'pinned_message': message.Message,
    'can_set_sticker_set': BasicType.bool_interpreter,
    'photo': chatphoto.ChatPhoto,
    'permissions': chatpermissions.ChatPermissions
})
