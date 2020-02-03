from . import BasicType
from . import polloption


class Poll(BasicType):
    fields = {
        'id': str,
        'question': str,
        'options': {
            'class': polloption.PollOption,
            'array': True
        },
        'total_voter_count': int,
        'is_closed': BasicType.bool_interpreter,
        'is_anonymous': BasicType.bool_interpreter,
        'type': str,
        'allows_multiple_answers': BasicType.bool_interpreter,
        'correct_option_id': int
    }

    def __init__(self, obj=None):
        super(Poll, self).__init__(obj)

