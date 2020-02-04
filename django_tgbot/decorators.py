from django_tgbot.exceptions import ProcessFailure
from django_tgbot.state_manager import state_types
from django_tgbot.state_manager.transition_condition import TransitionCondition
import inspect
from django_tgbot.state_manager.state_manager import StateManager


def processor(manager: StateManager, from_states=None, message_types=None, update_types=None,
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
            current_state = state.name
            try:
                func(bot=bot, update=update, state=state, *args, **kwargs)
                if success == state_types.Reset:
                    state.name = ''
                    state.save()
                elif success == state_types.Keep:
                    state.name = current_state
                    state.save()
                elif success is not None:
                    state.name = success
                    state.save()
            except ProcessFailure:
                if fail == state_types.Reset:
                    state.name = ''
                    state.save()
                elif fail == state_types.Keep:
                    state.name = current_state
                    state.save()
                elif fail is not None:
                    state.name = fail
                    state.save()

        altered_message_types = message_types
        altered_update_types = update_types

        if altered_message_types is None:
            altered_message_types = manager.default_message_types
        if altered_update_types is None:
            altered_update_types = manager.default_update_types

        manager.register_state(TransitionCondition(
            from_states=from_states,
            message_types=altered_message_types,
            exclude_message_types=exclude_message_types,
            update_types=altered_update_types,
            exclude_update_types=exclude_update_types,
        ), processor=function_runner)

        return function_runner

    return state_registrar
