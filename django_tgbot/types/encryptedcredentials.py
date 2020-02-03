from . import BasicType


class EncryptedCredentials(BasicType):
    fields = {
        'data': str,
        'hash': str,
        'secret': str
    }

    def __init__(self, obj=None):
        super(EncryptedCredentials, self).__init__(obj)

    def get_data(self) -> str:
        return getattr(self, 'data', None)

    def get_hash(self) -> str:
        return getattr(self, 'hash', None)

    def get_secret(self) -> str:
        return getattr(self, 'secret', None)