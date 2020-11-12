from typing import Optional

from django_tgbot.state_manager import message_types
from . import BasicType


class Message(BasicType):
    """
    Represents Telegram Message type:
        https://core.telegram.org/bots/api#message
    """
    fields = {
        'message_id': str,
        'date': str,
        'forward_from_message_id': str,
        'forward_signature': str,
        'forward_sender_name': str,
        'forward_date': str,
        'edit_date': str,
        'media_group_id': str,
        'author_signature': str,
        'text': str,
        'caption': str,
        'new_chat_title': str,
        'delete_chat_photo': BasicType.bool_interpreter,
        'group_chat_created': BasicType.bool_interpreter,
        'supergroup_chat_created': BasicType.bool_interpreter,
        'channel_chat_created': BasicType.bool_interpreter,
        'migrate_to_chat_id': str,
        'migrate_from_chat_id': str,
        'connected_website': str,
    }

    def __init__(self, obj=None):
        super(Message, self).__init__(obj)

    def type(self):
        field_checks = {
            'text': message_types.Text,
            'audio': message_types.Audio,
            'document': message_types.Document,
            'animation': message_types.Animation,
            'game': message_types.Game,
            'photo': message_types.Photo,
            'sticker': message_types.Sticker,
            'video': message_types.Video,
            'voice': message_types.Voice,
            'video_note': message_types.VideoNote,
            'contact': message_types.Contact,
            'dice': message_types.Dice,
            'location': message_types.Location,
            'venue': message_types.Venue,
            'poll': message_types.Poll,
            'new_chat_members': message_types.NewChatMembers,
            'left_chat_member': message_types.LeftChatMember,
            'new_chat_title': message_types.NewChatTitle,
            'new_chat_photo': message_types.NewChatPhoto,
            'delete_chat_photo': message_types.DeleteChatPhoto,
            'group_chat_created': message_types.GroupChatCreated,
            'supergroup_chat_created': message_types.SupergroupChatCreated,
            'channel_chat_created': message_types.ChannelChatCreated,
            'migrate_to_chat_id': message_types.MigrateToChatId,
            'migrate_from_chat_id': message_types.MigrateFromChatId,
            'pinned_message': message_types.PinnedMessage,
            'invoice': message_types.Invoice,
            'successful_payment': message_types.SuccessfulPayment,
            'passport_data': message_types.PassportData
        }

        for key in field_checks.keys():
            if getattr(self, key, None) is not None:
                return field_checks[key]
        return None

    def get_message_id(self) -> str:
        return getattr(self, 'message_id', None)

    def get_chat(self):
        return getattr(self, 'chat', None)

    def get_user(self):
        return getattr(self, 'from', None)

    def get_from(self):
        return self.get_user()

    def get_reply_to_message(self):
        return getattr(self, 'reply_to_message', None)

    def get_text(self) -> Optional[str]:
        return getattr(self, 'text', None)

    def get_caption(self) -> Optional[str]:
        return getattr(self, 'caption', None)

    def get_reply_markup(self):
        return getattr(self, 'reply_markup', None)


# Placed here to avoid import cycles
from . import user, chat, messageentity, audio, document, animation, game, photosize, \
    inlinekeyboardmarkup, passportdata, successfulpayment, invoice, poll, \
    venue, location, contact, videonote, voice, video, sticker, dice


Message.fields.update({
    'reply_to_message': Message,
    'pinned_message': Message,
    'from': user.User,
    'chat': chat.Chat,
    'forward_from': user.User,
    'forward_from_chat': chat.Chat,
    'entities': {
        'class': messageentity.MessageEntity,
        'array': True
    },
    'caption_entities': {
        'class': messageentity.MessageEntity,
        'array': True
    },
    'audio': audio.Audio,
    'document': document.Document,
    'animation': animation.Animation,
    'game': game.Game,
    'photo': {
        'class': photosize.PhotoSize,
        'array': True
    },
    'sticker': sticker.Sticker,
    'video': video.Video,
    'voice': voice.Voice,
    'video_note': videonote.VideoNote,
    'contact': contact.Contact,
    'dice': dice.Dice,
    'location': location.Location,
    'venue': venue.Venue,
    'poll': poll.Poll,
    'new_chat_members': {
        'class': user.User,
        'array': True
    },
    'left_chat_member': user.User,
    'new_chat_photo': {
        'class': photosize.PhotoSize,
        'array': True
    },
    'invoice': invoice.Invoice,
    'successful_payment': successfulpayment.SuccessfulPayment,
    'passport_data': passportdata.PassportData,
    'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup
})
