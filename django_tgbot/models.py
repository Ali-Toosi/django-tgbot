from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import json
from django.db import models
from django.db.models import CASCADE


class AbstractTelegramChat(models.Model):
    """
    Represents a `chat` type in Bot API:
        https://core.telegram.org/bots/api#chat
    """
    CHAT_TYPES = (
        ("private", "private"),
        ("group", "group"),
        ("supergroup", "supergroup"),
        ("channel", "channel")
    )

    telegram_id = models.CharField(max_length=128, unique=True)
    type = models.CharField(choices=CHAT_TYPES, max_length=128)
    title = models.CharField(max_length=512, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)

    def is_private(self):
        return self.type == self.CHAT_TYPES[0][0]

    class Meta:
        abstract = True

    def __str__(self):
        return "{} ({})".format(self.title, self.telegram_id)


class AbstractTelegramUser(models.Model):
    """
    Represented a `user` type in Bot API:
        https://core.telegram.org/bots/api#user
    """
    telegram_id = models.CharField(max_length=128, unique=True)
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)

    def get_chat_state(self, chat: AbstractTelegramChat):
        state = AbstractTelegramState.objects.get_or_create(
            telegram_user__telegram_id=self.telegram_id,
            telegram_chat__telegram_id=chat.telegram_id
        )
        return state

    def get_private_chat_state(self):
        state = AbstractTelegramState.objects.get_or_create(
            telegram_user__telegram_id=self.telegram_id,
            telegram_chat__telegram_id=self.telegram_id
        )
        return state

    class Meta:
        abstract = True

    def __str__(self):
        return "{} {} (@{})".format(self.first_name, self.last_name, self.username)


class AbstractTelegramState(models.Model):
    memory = models.TextField(null=True, blank=True, verbose_name="Memory in JSON format")
    waiting_for = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        abstract = True

    def get_memory(self):
        """
        Gives a python object as the memory for this state.
        Use the set_memory method to set an object as memory. If invalid JSON used as memory, it will be cleared
        upon calling this method.
        """
        if self.memory in [None, '']:
            return {}
        try:
            return json.loads(self.memory)
        except ValueError:
            self.memory = ''
            self.save()
            return {}

    def set_memory(self, obj):
        """
        Sets a python object as memory for the state, in JSON format.
        If given object cannot be converted to JSON, function call will be ignored.
        :param obj: The memory object to be stored
        """
        try:
            self.memory = json.dumps(obj)
            self.save()
        except ValueError:
            pass

    def update_memory(self, obj):
        """
        Updates the memory in the exact way a Python dictionary is updated. New keys will be added and
        existing keys' value will be updated.
        :param obj: The dictionary to update based on
        """
        if type(obj) != dict:
            raise ValueError("Passed object should be type of dict")
        memory = self.get_memory()
        memory.update(obj)
        self.set_memory(memory)

