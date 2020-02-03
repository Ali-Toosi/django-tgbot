from typing import Optional

from django_tgbot.types import chat
from . import BasicType


class CallbackQuery(BasicType):
    fields = {
        'id': str,
        'inline_message_id': str,
        'chat_instance': str,
        'data': str,
        'game_short_name': str
    }

    def __init__(self, obj=None):
        super(CallbackQuery, self).__init__(obj)

    def get_id(self) -> str:
        return getattr(self, 'id', None)

    def get_user(self):
        return getattr(self, 'from', None)

    def get_from(self):
        return self.get_user()

    def get_message(self):  # -> Optional[message.Message]:
        return getattr(self, 'message', None)

    def get_chat(self) -> Optional[chat.Chat]:
        if self.get_message() is None:
            return None
        return self.get_message().get_chat()

    def get_inline_message_id(self) -> Optional[str]:
        return getattr(self, 'inline_message_id', None)

    def get_data(self) -> Optional[str]:
        return getattr(self, 'data', None)

# Placed here to avoid import cycles

from . import user, message

CallbackQuery.fields.update({
    'from': user.User,
    'message': message.Message
})
