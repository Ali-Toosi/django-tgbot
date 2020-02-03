from . import BasicType


class Game(BasicType):
    fields = {
        'title': str,
        'description': str,
        'text': str
    }

    def __init__(self, obj=None):
        super(Game, self).__init__(obj)

    def get_title(self) -> str:
        return getattr(self, 'title', None)


# Placed here to avoid import cycles
from . import photosize, messageentity, animation

Game.fields.update({
    'photo': {
        'class': photosize.PhotoSize,
        'array': True
    },
    'text_entities': {
        'class': messageentity.MessageEntity,
        'array': True
    },
    'animation': animation.Animation
})

