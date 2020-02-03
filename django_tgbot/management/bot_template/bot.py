from django_tgbot.bot import AbstractTelegramBot
from django_tgbot.state_manager.state_manager import StateManager
from django_tgbot.types.update import Update
from . import bot_token
from .models import TelegramUser, TelegramChat, TelegramState


class TelegramBot(AbstractTelegramBot):
    def __init__(self, token, state_manager):
        super(TelegramBot, self).__init__(token, state_manager)
    
    def get_db_user(self, telegram_id):
        return TelegramUser.objects.get_or_create(telegram_id=telegram_id)[0]

    def get_db_chat(self, telegram_id):
        return TelegramChat.objects.get_or_create(telegram_id=telegram_id)[0]

    def get_db_state(self, db_user, db_chat):
        return TelegramState.objects.get_or_create(telegram_user=db_user, telegram_chat=db_chat)[0]
    
    def pre_processing(self, update: Update, user, db_user, chat, db_chat, state):
        super(TelegramBot, self).pre_processing(update, user, db_user, chat, db_chat, state)

    def post_processing(self, update: Update, user, db_user, chat, db_chat, state):
        super(TelegramBot, self).post_processing(update, user, db_user, chat, db_chat, state)


state_manager = StateManager()
bot = TelegramBot(bot_token, state_manager)

from . import processors
