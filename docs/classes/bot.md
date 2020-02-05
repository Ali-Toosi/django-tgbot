# Bot class

[Telegram Bot API](https://core.telegram.org/bots/api) has several types and methods, allowing clients to work with it.
 This class is designed to allow you work with the API's methods easily and in an IDE-friendly manner.
 
 All of the API methods (with regard to the API version mentioned in this doc) are implemented as Python functions in the `BotAPIUser` class and this class inherits from it.
 
 This class receives an [Update](../types/update.md) object and is responsible for finding the related [processors](../processors.md) and run them.
  However, it runs a `pre_processing` method before running those processors and a `post_processing` after it.
  
##### pre_processing:
 By default, it only saves the current [User](../models/telegram_user.md) (if any), [Chat](../models/telegram_chat.md) (if any) and the 
 [State](../models/telegram_state.md).
 
 You can change this method to do some other custom pre-processings.
 
 
##### post_processing:
 This will be an empty function in a fresh bot and will do nothing. You can implement it for custom functionality.
 
<hr>
 
## API Methods

The API methods on this class do not change any of the data you send and the name of the API method is exactly the same as 
the name of the Python function. The main purpose of implementing them is to be easy to use, since they give you a list of 
names and their parameters so you can easily make API calls, knowing exactly what parameters this method requires.

Most of them are also equipped with type hints to facilitate developing if you are using a modern IDE.

Each of the API methods return something upon successful or failed requests. If the request is successful, the response will be
a [Type](../types/README.md) and if it fails, the response will be a JSON object explaining the reason of failure. The Bot class
will convert this response:

* If the request is successful, it will return the according [Type](../types/README.md) object
* If the request fails, if will return a dict with the key `ok` equal to `False`

<hr>

#### Example
This is an API call using the Bot class which will be successful:
```python
result = bot.sendMessage(chat_id='93856968', text='This is django-tgbot!')
```
In this scenario, the `result` variable will have a [Message](../types/message.md) object since the output of the `sendMessage` method
will be the sent message. You can find the output for each API method in the [Telegram Bot API](https://core.telegram.org/bots/api) or
 you can use the method type hint in this package.

This other API call will fail since the text argument is required for this method:
```python
result = bot.sendMessage(chat_id='93856968')
```
and `result` will be:
```python
{
    'ok': False,
    'error_code': 400,
    'description': 'Bad Request: message text is empty'
}
```
 
<hr>
 
### Methods' Arguments

You should have a look at the API documentations while calling methods as they might have certain requirements on some arguments. For example, `parse_mode` argument on some methods,
only accepts a few fixed strings and inline keyboards have three optional fields that exactly one of them should be filled with a value.

Regarding the fixed values for arguments, some of the commonly used arguments are defined in the Bot class for you to use, instead of writing the string value:

* parse_mode:
    * `Bot.PARSE_MODE_MARKDOWN`
    * `Bot.PARSE_MODE_HTML`


* poll_type:
    * `Bot.POLL_TYPE_REGULAR`
    * `Bot.POLL_TYPE_QUIZ`

* chat_action:
    * `Bot.CHAT_ACTION_TYPING`
    * `Bot.CHAT_ACTION_PHOTO`
    * `Bot.CHAT_ACTION_VIDEO_RECORD`
    * `Bot.CHAT_ACTION_VIDEO_UPLOAD`
    * `Bot.CHAT_ACTION_AUDIO_RECORD`
    * `Bot.CHAT_ACTION_AUDIO_UPLOAD`
    * `Bot.CHAT_ACTION_DOCUMENT`
    * `Bot.CHAT_ACTION_LOCATION`
    * `Bot.CHAT_ACTION_VIDEO_NOTE_RECORD`
    * `Bot.CHAT_ACTION_VIDEO_NOTE_UPLOAD`


Furthermore, some arguments may only accept JSON objects or boolean values. You should be mindful of these by making sure you have
read the API docs on how you should use them.

In some cases, you might find it easier if you create the needed object as a [Type](../types/README.md) and then convert it do
a dict or JSON. For example, if you want to send a keyboard along with a message, you can create a [ReplyKeyboardMarkup](../types/replykeyboardmarkup.md)
and convert it to JSON and pass it through as the `reply_markup` argument. All of defined [Type](../types/README.md) in this package
have a `to_dict` method to convert that object to a dict object and a `to_json` to convert it to JSON. Additionally, there is a
`make_primitive` static method on [Type](../types/README.md)s that you can use to convert a single object to a dict or a list of 
objects to a list of dicts.
 
As a special case, `reply_markup` argument can be passed as a Type object instead of a JSON object and it will automatically be 
converted to JSON. This is because this argument is used a lot for a lot of methods and it will automatically converted to JSON to be
more convenient. <b>It is also fine if you want to send the JSON object and it still works appropriately.</b>   
 
<b>If you want to create a [Type](../types/README.md) object, you should use a method called `a` and not the default constructor.
 For more information please read its [docs](../types/README.md).</b>



 