from . import BasicType


class ResponseParameters(BasicType):
    fields = {
        'migrate_to_chat_id': str,
        'retry_after': int
    }

    def __init__(self, obj=None):
        super(ResponseParameters, self).__init__(obj)

