from typing import Optional

from . import BasicType


class Contact(BasicType):
    fields = {
        'phone_number': str,
        'first_name': str,
        'last_name': str,
        'user_id': str,
        'vcard': str
    }

    def __init__(self, obj=None):
        super(Contact, self).__init__(obj)

    def get_phone_number(self) -> str:
        return getattr(self, 'phone_number', None)

    def get_first_name(self) -> str:
        return getattr(self, 'first_name', None)

    def get_last_name(self) -> Optional[str]:
        return getattr(self, 'last_name', None)

    @classmethod
    def a(cls, phone_number: str, first_name: str, last_name: Optional[str] = None, user_id: Optional[str] = None,
          vcard: Optional[str] = None):
        return super().a(**locals())