from django.db import models
from django.db.models import CASCADE

from django_tgbot.models import AbstractTelegramUser, AbstractTelegramChat, AbstractTelegramState


class TelegramUser(AbstractTelegramUser):
    pass


class TelegramChat(AbstractTelegramChat):
    pass


class TelegramState(AbstractTelegramState):
    telegram_user = models.ForeignKey(TelegramUser, related_name='telegram_states', on_delete=CASCADE)
    telegram_chat = models.ForeignKey(TelegramChat, related_name='telegram_states', on_delete=CASCADE)

    class Meta:
        unique_together = ('telegram_user', 'telegram_chat')

