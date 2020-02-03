from . import BasicType


class PollOption(BasicType):
    fields = {
        'text': str,
        'voter_count': int
    }

    def __init__(self, obj=None):
        super(PollOption, self).__init__(obj)
