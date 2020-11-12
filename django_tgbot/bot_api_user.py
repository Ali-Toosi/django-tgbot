from typing import Union, List

import requests
import time
import json
import inspect

from django_tgbot.exceptions import BotAPIRequestFailure
from django_tgbot.types.botcommand import BotCommand
from django_tgbot.types.chat import Chat
from django_tgbot.types.chatmember import ChatMember
from django_tgbot.types.file import File
from django_tgbot.types.forcereply import ForceReply
from django_tgbot.types.inlinekeyboardmarkup import InlineKeyboardMarkup
from django_tgbot.types.message import Message
from django_tgbot.types.poll import Poll
from django_tgbot.types.replykeyboardmarkup import ReplyKeyboardMarkup
from django_tgbot.types.replykeyboardremove import ReplyKeyboardRemove
from django_tgbot.types.stickerset import StickerSet
from django_tgbot.types.update import Update
from django_tgbot.types.user import User
from django_tgbot.types.userprofilephotos import UserProfilePhotos


def create_params_from_args(args=None, exclude=None):
    """
    The args should usually be `locals()` and exclude should be the args you want to exclude
    'self' is automatically added to exclude list.
    :return: a dictionary made from the arguments
    """
    if args is None:
        args = {}
    if exclude is None:
        exclude = []
    if 'self' not in exclude:
        exclude.append('self')
    result = {}
    for arg in args.keys():
        if arg in exclude or args[arg] is None:
            continue
        if hasattr(args[arg], 'to_dict'):
            result[arg] = args[arg].to_dict()
        else:
            result[arg] = args[arg]

        if arg == 'reply_markup' and type(result[arg]) != str:
            result[arg] = json.dumps(result[arg])

        if (type(result[arg])) == list:
            to_be_json_list = []
            for item in result[arg]:
                if hasattr(item, 'to_dict'):
                    to_be_json_list.append(item.to_dict())
                else:
                    to_be_json_list.append(item)

            result[arg] = json.dumps(to_be_json_list)

    return result


class BotAPIUser:
    MAX_TRIES = 5

    PARSE_MODE_MARKDOWN = 'Markdown'
    PARSE_MODE_HTML = 'HTML'

    POLL_TYPE_QUIZ = 'quiz'
    POLL_TYPE_REGULAR = 'regular'

    CHAT_ACTION_TYPING = 'typing'
    CHAT_ACTION_PHOTO = 'upload_photo'
    CHAT_ACTION_VIDEO_RECORD = 'record_video'
    CHAT_ACTION_VIDEO_UPLOAD = 'upload_video'
    CHAT_ACTION_AUDIO_RECORD = 'record_audio'
    CHAT_ACTION_AUDIO_UPLOAD = 'upload_audio'
    CHAT_ACTION_DOCUMENT = 'upload_document'
    CHAT_ACTION_LOCATION = 'find_location'
    CHAT_ACTION_VIDEO_NOTE_RECORD = 'record_video_note'
    CHAT_ACTION_VIDEO_NOTE_UPLOAD = 'upload_video_note'

    def __init__(self, token):
        self.token = ''
        self.api_url = ''
        self.set_token(token)

    def set_token(self, token):
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}'.format(self.token)

    def send_request(self, method, data=None, files=None):
        if data is None:
            data = {}
        url = '{}/{}'.format(self.api_url, method)
        r = None
        sleep_time = 1
        for i in range(self.MAX_TRIES):
            try:
                if files is None:
                    r = requests.post(url, data)
                else:
                    r = requests.post(url, data=data, files=files)
            except requests.RequestException:
                time.sleep(sleep_time)
                sleep_time += 0.2
                continue
            else:
                break

        if r is not None:
            python_result = json.loads(r.text)
            if 'ok' not in python_result:
                python_result['ok'] = bool(r)
            return python_result
        return {'ok': False, 'description': 'Max tries exceeded.', 'no_connection': True}

    def request_and_result(self, data, result_type, files=None):
        """
        Should be called by a method with exact same name as the API method

        :param result_type: can be either a type class or a list containing one type class which will parse
            the result to be a list of that type. For example: Message if the result is a message or [Message] if the
            result if a list of messages
        """
        res = self.send_request(inspect.stack()[1].function, data=data, files=files)
        if res['ok']:
            if type(result_type) == list and len(result_type) > 0:
                if len(result_type) > 1:
                    raise ValueError("Passed `result_type` cannot have more than one element if it is a list.")
                return list(map(result_type[0], list(res['result'])))
            else:
                return result_type(res['result'])
        else:
            return res

    def getMe(self) -> User:
        return self.request_and_result(create_params_from_args(), User)

    def getMyCommands(self) -> List[BotCommand]:
        return self.request_and_result(create_params_from_args(), [BotCommand])

    def setMyCommands(self, commands: List[BotCommand]) -> bool:
        return self.request_and_result(create_params_from_args(locals()), bool)

    def getUpdates(self, offset=None, limit=100, timeout=0, allow_updates=None) -> List[Update]:
        """
        Returns a list of UNPARSED updates. The json objects in the list should still be sent to Update class to become
        Update objects.
        :param offset: The update_id of the first update you wish to receive
        :param limit: The number of updates returned
        :param timeout: Timeout in seconds for long polling.
        :param allow_updates: List of the update types you want your bot to receive. Can be either a list of JSON string
        :return: a list of json updates
        """
        updates = self.request_and_result(create_params_from_args(locals()), [Update])
        if type(updates) == dict and not updates['ok']:
            raise BotAPIRequestFailure(f"Error code {updates['error_code']} ({updates['description']})")
        return updates

    def setWebhook(self, url):
        return self.send_request('setWebhook', {'url': url})

    def sendMessage(self, chat_id, text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                    reply_to_message_id=None,
                    reply_markup: Union[
                        None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:
        return self.request_and_result(create_params_from_args(locals()), Message)

    def forwardMessage(self, chat_id, from_chat_id, message_id, disable_notification=None):
        return self.request_and_result(create_params_from_args(locals()), Message)

    def sendPhoto(self, chat_id, photo, upload=False, caption=None, parse_mode=None, disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup: Union[
                      None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:
        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'photo']),
                Message,
                files={'photo': photo}
            )

    def sendAudio(self, chat_id, audio, upload=False, caption=None, parse_mode=None, duration=None, performer=None,
                  title=None,
                  thumb=None, disable_notification=None, reply_to_message_id=None,
                  reply_markup: Union[
                      None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'audio']),
                Message,
                files={'audio': audio}
            )

    def sendDocument(self, chat_id, document, upload=False, thumb=None, caption=None, parse_mode=None,
                     disable_notification=None,
                     reply_to_message_id=None,
                     reply_markup: Union[
                         None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'document']),
                Message,
                files={'document': document}
            )

    def sendVideo(self, chat_id, video, upload=False, duration=None, width=None, height=None, thumb=None, caption=None,
                  parse_mode=None, supports_streaming=None, disable_notification=None, reply_to_message_id=None,
                  reply_markup: Union[
                      None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'video']),
                Message,
                files={'video': video}
            )

    def sendAnimation(self, chat_id, animation, upload=False, duration=None, width=None, height=None, thumb=None,
                      caption=None,
                      parse_mode=None, disable_notification=None, reply_to_message_id=None,
                      reply_markup: Union[
                          None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'animation']),
                Message,
                files={'animation': animation}
            )

    def sendVoice(self, chat_id, voice, upload=False, caption=None, parse_mode=None, duration=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup: Union[
                      None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'voice']),
                Message,
                files={'voice': voice}
            )

    def sendVideoNote(self, chat_id, video_note, upload=False, duration=None, length=None, thumb=None,
                      disable_notification=None,
                      reply_to_message_id=None,
                      reply_markup: Union[
                          None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'video_note']),
                Message,
                files={'video_note': video_note}
            )

    def sendMediaGroup(self, chat_id, media, upload=False, disable_notification=None, reply_to_message_id=None):
        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'media']),
                Message,
                files={'media': media}
            )

    def sendLocation(self, chat_id, latitude, longitude, live_period=None, disable_notification=None,
                     reply_to_message_id=None,
                     reply_markup: Union[
                         None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def editMessageLiveLocation(self, chat_id, latitude, longitude, message_id=None, inline_message_id=None,
                                reply_markup: Union[
                                    None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def stopMessageLiveLocation(self, chat_id, message_id=None, inline_message_id=None,
                                reply_markup: Union[
                                    None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def sendVenue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None,
                  disable_notification=None, reply_to_message_id=None,
                  reply_markup: Union[
                      None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def sendContact(self, chat_id, phone_number, first_name, last_name=None, vcard=None, disable_notification=None,
                    reply_to_message_id=None,
                    reply_markup: Union[
                        None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def sendPoll(self, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None,
                 correct_option_id=None, is_closed=None, disable_notification=None, reply_to_message_id=None,
                 reply_markup: Union[
                     None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:
        return self.request_and_result(create_params_from_args(locals()), Message)

    def sendChatAction(self, chat_id, action):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def getUserProfilePhotos(self, user_id, offset=None, limit=None):
        return self.request_and_result(create_params_from_args(locals()), UserProfilePhotos)

    def getFile(self, file_id):
        return self.request_and_result(create_params_from_args(locals()), File)

    def kickChatMember(self, chat_id, user_id, until_date=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def unbanChatMember(self, chat_id, user_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def restrictChatMember(self, chat_id, user_id, permissions, until_date=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def promoteChatMember(self, chat_id, user_id, can_change_info=None, can_post_messages=None, can_edit_messages=None,
                          can_delete_messages=None, can_invite_users=None, can_restrict_members=None,
                          can_pin_messages=None, can_promote_members=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def setChatAdministratorCustomTitle(self, chat_id, user_id, custom_title):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def setChatPermissions(self, chat_id, permissions):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def exportChatInviteLink(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def setChatPhoto(self, chat_id, photo):
        return self.request_and_result(create_params_from_args(locals(), ['photo']), bool, files={'photo': photo})

    def deleteChatPhoto(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def setChatTitle(self, chat_id, title):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def setChatDescription(self, chat_id, description=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def pinChatMessage(self, chat_id, message_id, disable_notification=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def unpinChatMessage(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def leaveChat(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def getChat(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), Chat)

    # TODO getChatAdministrators

    def getChatMembersCount(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), int)

    def getChatMember(self, chat_id, user_id):
        return self.request_and_result(create_params_from_args(locals()), ChatMember)

    def setChatStickerSet(self, chat_id, sticker_set_name):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def deleteChatStickerSet(self, chat_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def answerCallbackQuery(self, callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def editMessageText(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                        disable_webpage_preview=None,
                        reply_markup: Union[
                            None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def editMessageCaption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None, parse_mode=None,
                           reply_markup: Union[
                               None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def editMessageMedia(self, media, chat_id=None, message_id=None, inline_message_id=None,
                         reply_markup: Union[
                             None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def editMessageReplyMarkup(self, chat_id=None, message_id=None, inline_message_id=None,
                               reply_markup: Union[
                                   None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def stopPoll(self, chat_id, message_id, reply_markup=None):
        return self.request_and_result(create_params_from_args(locals()), Poll)

    def deleteMessage(self, chat_id, message_id):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def sendSticker(self, chat_id, sticker, upload=False, disable_notification=None, reply_to_message_id=None,
                    reply_markup: Union[
                        None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), Message)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'sticker']),
                Message,
                files={'sticker': sticker}
            )

    def getStickerSet(self, name):
        return self.request_and_result(create_params_from_args(locals()), StickerSet)

    def uploadStickerFile(self, user_id, png_sticker):
        return self.request_and_result(create_params_from_args(locals(), ['png_sticker']), File,
                                       files={'png_sticker': png_sticker})

    def createNewStickerSet(self, user_id, name, title, emojis, png_sticker=None, tgs_sticker=None, upload=False,
                            contains_masks=None, mask_position=None):
        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), bool)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'png_sticker']),
                bool,
                files={'png_sticker': png_sticker}
            )

    def addStickerToSet(self, user_id, name, emojis, png_sticker=None, tgs_sticker=None, upload=False, mask_position=None):
        if not upload:
            return self.request_and_result(create_params_from_args(locals(), ['upload']), bool)
        else:
            return self.request_and_result(
                create_params_from_args(locals(), ['upload', 'png_sticker']),
                bool,
                files={'png_sticker': png_sticker}
            )

    def setStickerPositionInSet(self, sticker, position):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def deleteStickerFromSet(self, sticker):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def answerInlineQuery(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                          switch_pm_text=None, switch_pm_parameter=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def sendInvoice(self, chat_id, title, description, payload, provider_token, start_parameter, currency, prices,
                    provider_data=None, photo_url=None, photo_size=None, photo_width=None, photo_height=None,
                    need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None,
                    send_phone_number_to_provider=None, send_email_to_provider=None, is_flexible=None,
                    disable_notification=None, reply_to_message_id=None,
                    reply_markup: Union[
                        None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None) -> Message:

        return self.request_and_result(create_params_from_args(locals()), Message)

    def answerShippingQuery(self, shipping_query_id, ok, shipping_options=None, error_message=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def answerPreCheckoutQuery(self, pre_checkout_query_id, ok, error_message=None):
        return self.request_and_result(create_params_from_args(locals()), bool)

    def sendGame(self, chat_id, game_short_name, disable_notification=None, reply_to_message_id=None,
                 reply_markup=None):
        return self.request_and_result(create_params_from_args(locals()), Message)

    def setGameScore(self, user_id, score, force=None, disable_edit_message=None, chat_id=None, message_id=None,
                     inline_message_id=None):
        return self.request_and_result(create_params_from_args(locals()), Message)

    # TODO getGameHighScores

    def sendDice(
            self, chat_id, emoji=None, disable_notification=None, reply_to_message_id=None,
            allow_sending_without_reply=None, reply_markup: Union[
                    None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None):
        return self.request_and_result(create_params_from_args(locals()), Message)


