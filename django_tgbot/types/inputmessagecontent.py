from typing import Optional

from . import BasicType


class InputMessageContent(BasicType):
    def __init__(self, obj=None):
        super(InputMessageContent, self).__init__(obj)


class InputTextMessageContent(InputMessageContent):
    fields = {
        'message_text': str,
        'parse_mode': str,
        'disable_web_page_preview': BasicType.bool_interpreter
    }

    def __init__(self, obj=None):
        super(InputTextMessageContent, self).__init__(obj)

    @classmethod
    def a(cls, message_text: str,
          parse_mode: Optional[str] = None, disable_web_page_preview: Optional[bool] = None):
        return super().a(**locals())


class InputLocationMessageContent(InputMessageContent):
    fields = {
        'latitude': str,
        'longitude': str,
        'live_period': int
    }

    def __init__(self, obj=None):
        super(InputLocationMessageContent, self).__init__(obj)

    @classmethod
    def a(cls, latitude: str, longitude: str, live_period: Optional[int] = None):
        return super().a(**locals())


class InputVenueMessageContent(InputMessageContent):
    fields = {
        'latitude': str,
        'longitude': str,
        'title': str,
        'address': str,
        'foursquare_id': str,
        'foursquare_type': str
    }

    def __init__(self, obj=None):
        super(InputVenueMessageContent, self).__init__(obj)

    @classmethod
    def a(cls, latitude: str, longitude: str, title: str, address: str, foursquare_id: Optional[str] = None,
          foursquare_type: Optional[str] = None):
        return super().a(**locals())


class InputContactMessageContent(InputMessageContent):
    fields = {
        'phone_number': str,
        'first_name': str,
        'last_name': str,
        'vcard': str
    }

    def __init__(self, obj=None):
        super(InputContactMessageContent, self).__init__(obj)

    @classmethod
    def a(cls, phone_number: str, first_name: str, last_name: Optional[str] = None, vcard: Optional[str] = None):
        return super().a(**locals())


