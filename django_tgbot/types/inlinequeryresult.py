from typing import Optional

from . import BasicType
from . import inputmessagecontent, inlinekeyboardmarkup


class InlineQueryResult(BasicType):
    def __init__(self, obj=None):
        super(InlineQueryResult, self).__init__(obj)


class InlineQueryResultArticle(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'title': str,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        },
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'url': str,
        'hide_url': BasicType.bool_interpreter,
        'description': str,
        'thumb_url': str,
        'thumb_width': int,
        'thumb_height': int
    }

    def __init__(self, obj=None):
        super(InlineQueryResultArticle, self).__init__(obj)

    @classmethod
    def a(cls, id: str, title: str, input_message_content: inputmessagecontent.InputMessageContent,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None, url: Optional[str] = None,
          hide_url: Optional[bool] = None, description: Optional[str] = None, thumb_url: Optional[str] = None,
          thumb_width: Optional[int] = None, thumb_height: Optional[int] = None):
        type = 'article'
        return super().a(**locals())


class InlineQueryResultPhoto(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'photo_url': str,
        'thumb_url': str,
        'photo_width': int,
        'photo_height': int,
        'title': str,
        'description': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultPhoto, self).__init__(obj)

    @classmethod
    def a(cls, id: str, photo_url: str, thumb_url: str, photo_width: Optional[int] = None,
          photo_height: Optional[int] = None, title: Optional[str] = None, description: Optional[str] = None,
          caption: Optional[str] = None, parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'photo'
        return super().a(**locals())


class InlineQueryResultGif(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'gif_url': str,
        'gif_width': int,
        'gif_height': int,
        'gif_duration': int,
        'thumb_url': str,
        'thumb_mime_type': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultGif, self).__init__(obj)

    @classmethod
    def a(cls, id: str, gif_url: str, thumb_url: str, thumb_mime_type: str = None, gif_width: Optional[int] = None, gif_height: Optional[int] = None,
          gif_duration: Optional[int] = None, title: Optional[str] = None, caption: Optional[str] = None,
          parse_mode: Optional[str] = None, input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'gif'
        return super().a(**locals())


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'mpeg4_url': str,
        'mpeg4_width': int,
        'mpeg4_height': int,
        'mpeg4_duration': int,
        'thumb_url': str,
        'thumb_mime_type': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultMpeg4Gif, self).__init__(obj)

    @classmethod
    def a(cls, id: str, mpeg4_url: str, thumb_url: str, thumb_mime_type: str = None, mpeg4_width: Optional[int] = None,
          mpeg4_height: Optional[int] = None, mpeg4_duration: Optional[int] = None, title: Optional[str] = None,
          caption: Optional[str] = None, parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'mpeg4_gif'
        return super().a(**locals())


class InlineQueryResultVideo(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'video_url': str,
        'mime_type': str,
        'thumb_url': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'video_width': int,
        'video_height': int,
        'video_duration': int,
        'description': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultVideo, self).__init__(obj)

    @classmethod
    def a(cls, id: str, video_url: str, mime_type: str, thumb_url: str, title: str,
          caption: Optional[str] = None, parse_mode: Optional[str] = None, video_width: Optional[int] = None,
          video_height: Optional[int] = None, video_duration: Optional[int] = None, description: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'video'
        return super().a(**locals())


class InlineQueryResultAudio(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'audio_url': str,
        'title': str,
        'caption': str,
        'performer': str,
        'audio_duration': int,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultAudio, self).__init__(obj)

    @classmethod
    def a(cls, id: str, audio_url: str, title: str, caption: Optional[str] = None,
          parse_mode: Optional[str] = None, performer: Optional[str] = None, audio_duration: Optional[int] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'audio'
        return super().a(**locals())


class InlineQueryResultVoice(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'voice_url': str,
        'voice_duration': int,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultVoice, self).__init__(obj)

    @classmethod
    def a(cls, id: str, voice_url: str, title: str, caption: Optional[str] = None,
          parse_mode: Optional[str] = None, voice_duration: Optional[int] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'voice'
        return super().a(**locals())


class InlineQueryResultDocument(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'document_url': str,
        'mime_type': str,
        'description': str,
        'thumb_url': str,
        'thumb_width': int,
        'thumb_height': int,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultDocument, self).__init__(obj)

    @classmethod
    def a(cls, id: str, title: str, document_url: str, mime_type: str, caption: Optional[str] = None,
          parse_mode: Optional[str] = None, description: Optional[str] = None, thumb_url: Optional[str] = None,
          thumb_width: Optional[int] = None, thumb_height: Optional[int] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'document'
        return super().a(**locals())


class InlineQueryResultLocation(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'latitude': str,
        'longitude': str,
        'title': str,
        'live_period': int,
        'thumb_width': int,
        'thumb_height': int,
        'thumb_url': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultLocation, self).__init__(obj)

    @classmethod
    def a(cls, id: str, latitude: str, longitude: str, title: str, live_period: Optional[int] = None,
          thumb_url: Optional[str] = None, thumb_width: Optional[int] = None, thumb_height: Optional[int] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'document'
        return super().a(**locals())


class InlineQueryResultVenue(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'latitude': str,
        'longitude': str,
        'title': str,
        'address': str,
        'foursquare_id': str,
        'foursquare_type': str,
        'thumb_url': str,
        'thumb_width': int,
        'thumb_height': int,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultVenue, self).__init__(obj)

    @classmethod
    def a(cls, id: str, latitude: str, longitude: str, title: str, address: str,
          foursquare_id: Optional[str] = None, foursqure_type: Optional[str] = None, thumb_url: Optional[str] = None,
          thumb_width: Optional[int] = None, thumb_height: Optional[int] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'venue'
        return super().a(**locals())


class InlineQueryResultContact(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'phone_number': str,
        'first_name': str,
        'last_name': str,
        'vcard': str,
        'thumb_url': str,
        'thumb_width': int,
        'thumb_height': int,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultContact, self).__init__(obj)

    @classmethod
    def a(cls, id: str, phone_number: str, first_name: str, last_name: Optional[str] = None,
          vcard: Optional[str] = None, thumb_url: Optional[str] = None, thumb_width: Optional[int] = None,
          thumb_height: Optional[int] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'contact'
        return super().a(**locals())


class InlineQueryResultGame(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'game_short_name': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
    }

    def __init__(self, obj=None):
        super(InlineQueryResultGame, self).__init__(obj)

    @classmethod
    def a(cls, id: str, game_short_name: str,
        reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'game'
        return super().a(**locals())


class InlineQueryResultCachedPhoto(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'photo_file_id': str,
        'description': str,
        'thumb_url': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedPhoto, self).__init__(obj)

    @classmethod
    def a(cls, id: str, photo_file_id: str, title: Optional[str] = None,
          description: Optional[str] = None, caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'photo'
        return super().a(**locals())


class InlineQueryResultCachedGif(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'gif_file_id': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedGif, self).__init__(obj)

    @classmethod
    def a(cls, id: str, gif_file_id: str, title: Optional[str] = None,
          caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'gif'
        return super().a(**locals())


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'mpeg4_file_id': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedMpeg4Gif, self).__init__(obj)

    @classmethod
    def a(cls, id: str, mpeg4_file_id: str, title: Optional[str] = None,
          caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'mpeg4_gif'
        return super().a(**locals())


class InlineQueryResultCachedSticker(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'sticker_file_id': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedSticker, self).__init__(obj)

    @classmethod
    def a(cls, id: str, sticker_file_id: str,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'sticker'
        return super().a(**locals())


class InlineQueryResultCachedDocument(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'title': str,
        'caption': str,
        'description': str,
        'document_file_id': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedDocument, self).__init__(obj)

    @classmethod
    def a(cls, id: str, document_file_id: str, title: str,
          description: Optional[str] = None, caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'document'
        return super().a(**locals())


class InlineQueryResultCachedVideo(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'video_file_id': str,
        'title': str,
        'caption': str,
        'description': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedVideo, self).__init__(obj)

    @classmethod
    def a(cls, id: str, video_file_id: str, title: str,
          description: Optional[str] = None, caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'video'
        return super().a(**locals())


class InlineQueryResultCachedVoice(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'voice_file_id': str,
        'title': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedVoice, self).__init__(obj)

    @classmethod
    def a(cls, id: str, voice_file_id: str, title: str,
          caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'voice'
        return super().a(**locals())


class InlineQueryResultCachedAudio(InlineQueryResult):
    fields = {
        'type': str,
        'id': str,
        'audio_file_id': str,
        'caption': str,
        'parse_mode': str,
        'reply_markup': inlinekeyboardmarkup.InlineKeyboardMarkup,
        'input_message_content': {
            'class': inputmessagecontent.InputMessageContent,
            'validation': False
        }
    }

    def __init__(self, obj=None):
        super(InlineQueryResultCachedAudio, self).__init__(obj)

    @classmethod
    def a(cls, id: str, audio_file_id: str,
          caption: Optional[str] = None,
          parse_mode: Optional[str] = None,
          input_message_content: Optional[inputmessagecontent.InputMessageContent] = None,
          reply_markup: Optional[inlinekeyboardmarkup.InlineKeyboardMarkup] = None):
        type = 'audio'
        return super().a(**locals())
