from django_tgbot.models import AbstractTelegramState
from django_tgbot.state_manager.state import State
from django_tgbot.types.update import Update


class StateManager:
    def __init__(self):
        self.handling_states = {}

    def register_state(self, state: State, processor):
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
        waiting_for = state.waiting_for
        processors = []
        for state in self.handling_states.keys():
            if state.matches(waiting_for=waiting_for, update_type=update_type, message_type=message_type):
                processors.append(self.handling_states[state])
        return processors

