from . import BasicType


class GameHighScore(BasicType):
    fields = {
        'position': int,
        'score': int
    }

    def __init__(self, obj=None):
        super(GameHighScore, self).__init__(obj)

    def get_user(self):  # -> user.User:
        return getattr(self, 'user', None)

    def get_score(self) -> int:
        return getattr(self, 'score', None)


from . import user

GameHighScore.fields.update({
    'user': user.User,
})