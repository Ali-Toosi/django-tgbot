from typing import Optional, List

from . import BasicType
from . import passportfile


class EncryptedPassportElement(BasicType):
    fields = {
        'type': str,
        'data': str,
        'phone_number': str,
        'email': str,
        'files': {
            'class': passportfile.PassportFile,
            'array': True
        },
        'front_side': passportfile.PassportFile,
        'reverse_side': passportfile.PassportFile,
        'selfie': passportfile.PassportFile,
        'translation': {
            'class': passportfile.PassportFile,
            'array': True
        },
        'hash': str
    }

    def __init__(self, obj=None):
        super(EncryptedPassportElement, self).__init__(obj)

    def get_type(self) -> str:
        return getattr(self, 'type', None)

    def get_data(self) -> Optional[str]:
        return getattr(self, 'data', None)

    def get_files(self) -> Optional[List[passportfile.PassportFile]]:
        return getattr(self, 'files', None)
