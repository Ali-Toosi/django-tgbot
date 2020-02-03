from . import BasicType


class PollAnswer(BasicType):
    fields = {
        'poll_id': str,
        'option_ids': {
            'class': int,
            'array': True
        },
    }

    def __init__(self, obj=None):
        super(PollAnswer, self).__init__(obj)

    def get_user(self):
        return getattr(self, 'user', None)


from . import user

PollAnswer.fields.update({
    'user': user.User
})