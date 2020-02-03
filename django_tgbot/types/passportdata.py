from . import BasicType
from . import encryptedpassportelement, encryptedcredentials


class PassportData(BasicType):
    fields = {
        'data': {
            'class': encryptedpassportelement.EncryptedPassportElement,
            'array': True
        },
        'credentials': encryptedcredentials.EncryptedCredentials
    }

    def __init__(self, obj=None):
        super(PassportData, self).__init__(obj)
