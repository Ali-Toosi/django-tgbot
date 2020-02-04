from django_tgbot.models import AbstractTelegramState
from django_tgbot.state_manager.transition_condition import TransitionCondition
from django_tgbot.types.update import Update


class StateManager:
    def __init__(self):
        self.handling_states = {}
        self.default_message_types = None
        self.default_update_types = None

    def register_state(self, state: TransitionCondition, processor):
        self.handling_states[state] = processor

    def get_processors(self, update: Update, state: AbstractTelegramState):
        """
        Searches through all of the processors and creates a list of those that handle the current state
        :param update: The received update
        :param state: The current state
        :return: a list of processors
        """
        message = update.get_message()
        message_type = message.type() if message is not None else None
        update_type = update.type()
        state_name = state.name
        processors = []
        for state in self.handling_states.keys():
            if state.matches(state_name=state_name, update_type=update_type, message_type=message_type):
                processors.append(self.handling_states[state])
        return processors

    def set_default_message_types(self, message_types):
        self.default_message_types = message_types

    def set_default_update_types(self, update_types):
        self.default_update_types = update_types

