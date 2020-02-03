from django_tgbot.state_manager import update_types
from django_tgbot.types import chat
from . import BasicType
from . import message, inlinequery, choseninlineresult, callbackquery, shippingquery, precheckoutquery, poll, pollanswer


class Update(BasicType):
    fields = {
        'update_id': str,
        'message': message.Message,
        'edited_message': message.Message,
        'channel_post': message.Message,
        'edited_channel_post': message.Message,
        'inline_query': inlinequery.InlineQuery,
        'chosen_inline_result': choseninlineresult.ChosenInlineResult,
        'callback_query': callbackquery.CallbackQuery,
        'shipping_query': shippingquery.ShippingQuery,
        'pre_checkout_query': precheckoutquery.PreCheckoutQuery,
        'poll': poll.Poll,
        'poll_answer': pollanswer.PollAnswer
    }

    def __init__(self, obj=None):
        super(Update, self).__init__(obj)

    def type(self):
        field_checks = {
            'message': update_types.Message,
            'edited_message': update_types.EditedMessage,
            'channel_post': update_types.ChannelPost,
            'edited_channel_post': update_types.EditedChannelPost,
            'inline_query': update_types.InlineQuery,
            'chosen_inline_result': update_types.ChosenInlineResult,
            'callback_query': update_types.CallbackQuery,
            'shipping_query': update_types.ShippingQuery,
            'pre_checkout_query': update_types.PreCheckoutQuery,
            'poll': update_types.Poll,
            'poll_answer': update_types.PollAnswer
        }
        for key in field_checks.keys():
            if getattr(self, key, None) is not None:
                return field_checks[key]
        return None

    def get_message(self) -> message.Message or None:
        for key in ['message', 'edited_message', 'channel_post', 'edited_channel_post']:
            if getattr(self, key, None) is not None:
                return getattr(self, key, None)
        return None

    def get_chat(self) -> chat.Chat or None:
        if self.get_message() is not None:
            return self.get_message().get_chat()
        if self.is_callback_query():
            return self.get_callback_query().get_chat()
        return None

    def get_user(self):
        if self.get_message() is not None:
            return self.get_message().get_user()
        if self.is_inline_query():
            return self.get_inline_query().get_user()
        if self.is_chosen_inline_result():
            return self.get_chosen_inline_result().get_user()
        if self.is_callback_query():
            return self.get_callback_query().get_user()
        if self.is_shipping_query():
            return self.get_shipping_query().get_user()
        if self.is_pre_checkout_query():
            return self.get_pre_checkout_query().get_user()
        if self.is_poll_answer():
            return self.get_poll_answer().get_user()
        return None

    def get_callback_query(self) -> callbackquery.CallbackQuery:
        return getattr(self, 'callback_query', None)

    def get_inline_query(self) -> inlinequery.InlineQuery:
        return getattr(self, 'inline_query', None)

    def get_shipping_query(self) -> shippingquery.ShippingQuery:
        return getattr(self, 'shipping_query', None)

    def get_chosen_inline_result(self) -> choseninlineresult.ChosenInlineResult:
        return getattr(self, 'chosen_inline_result', None)

    def get_pre_checkout_query(self) -> precheckoutquery.PreCheckoutQuery:
        return getattr(self, 'pre_checkout_query', None)

    def get_poll_answer(self) -> pollanswer.PollAnswer:
        return getattr(self, 'poll_answer', None)

    def is_poll_answer(self):
        return self.get_poll_answer() is not None

    def is_pre_checkout_query(self):
        return self.get_pre_checkout_query() is not None

    def is_chosen_inline_result(self):
        return self.get_chosen_inline_result() is not None

    def is_inline_query(self):
        return self.get_inline_query() is not None

    def is_callback_query(self):
        return self.get_callback_query() is not None

    def is_shipping_query(self):
        return self.get_shipping_query() is not None
