from . import BasicType


class BotCommand(BasicType):
    fields = {
        'command': str,
        'description': str
    }

    def __init__(self, obj=None):
        super(BotCommand, self).__init__(obj)

    def get_command(self) -> str:
        return getattr(self, 'command')

    def get_description(self) -> str:
        return getattr(self, 'description')

    @classmethod
    def a(cls, command: str, description: str):
        command = str(command).lower()
        return super().a(**locals())
