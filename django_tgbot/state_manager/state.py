from django_tgbot.state_manager import state_types


class State:
    def __init__(self, waiting_for=None, message_types=None, update_types=None, exclude_message_types=None,
                 exclude_update_types=None):
        """
        Leave message_types / update_types for accepting all.
        :param waiting_for: the user's state in database
        :param message_types: accepted message_types
        :param update_types: accepted update_types
        """
        if message_types in ['all', '*', state_types.All]:
            message_types = None

        if update_types in ['all', '*', state_types.All]:
            update_types = None

        if waiting_for is None:
            waiting_for = ['', None]
        elif waiting_for in ['*', state_types.All]:
            waiting_for = ['*']

        args = locals()
        for var in args.keys():
            if var == 'self':
                continue

            result = args[var]
            if args[var] is None:
                result = []
            elif type(args[var]) == str:
                result = [args[var]]

            if type(result) != list:
                raise ValueError("Type of `{}` should be list".format(var))

            setattr(self, var, result)

    def matches(self, waiting_for, update_type, message_type=None):
        try:
            return (waiting_for in self.waiting_for or self.waiting_for == ['*']) and \
                   (message_type is None or message_type in self.message_types or self.message_types == []) and \
                   (message_type is None or message_type not in self.exclude_message_types) and \
                   (update_type in self.update_types or self.update_types == []) and \
                   (update_type not in self.exclude_update_types)
        except AttributeError:
            return False
