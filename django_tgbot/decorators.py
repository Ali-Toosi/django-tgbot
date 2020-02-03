from django_tgbot.state_manager import state_types
from django_tgbot.state_manager.state import State
import inspect
from django_tgbot.state_manager.state_manager import StateManager


def bot_state(manager: StateManager, waiting_for=None, message_types=None, update_types=None,
              exclude_message_types=None, exclude_update_types=None, success=None, fail=None):
    def state_registrar(func):
        if func is None:
            raise ValueError("Passed processor is None.")
        all_args = inspect.getfullargspec(func)
        if not all([
            x in all_args[0] for x in ['bot', 'update', 'state']
        ]):
            raise ValueError("Passed processor does not have a valid signature.")

        def function_runner(bot, update, state, *args, **kwargs):
            try:
                func(bot, update, state, *args, **kwargs)
                if success != state_types.Keep:
                    state.waiting_for = success
                state.save()
            except Exception as e:
                if fail != state_types.Keep:
                    state.waiting_for = fail
                state.save()

        manager.register_state(State(
            waiting_for=waiting_for,
            message_types=message_types,
            exclude_message_types=exclude_message_types,
            update_types=update_types,
            exclude_update_types=exclude_update_types,
        ), processor=function_runner)

        return function_runner

    return state_registrar
