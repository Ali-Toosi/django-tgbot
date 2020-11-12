# Bot class

[Telegram Bot API](https://core.telegram.org/bots/api) has several types and methods.
This class is designed to allow you to work with the Telegram's API methods easily and in an IDE-friendly manner.
 
All of the API methods (with regard to the API version mentioned in this doc) are implemented as Python functions in the `BotAPIUser` class and this class inherits from it.
 
This class receives an [Update](../types/update.md) object and is responsible for finding the related [processors](../processors.md) and run them.
However, it runs a `pre_processing` method before running those processors and a `post_processing` after it.
  
<b>pre_processing</b>

By default, it only saves the current [User](../models/telegram_user.md) (if any), [Chat](../models/telegram_chat.md) (if any) and the 
[State](../models/telegram_state.md).
 
You can change this method to do some other custom pre-processings.
 
 
<b>post_processing</b>

This will be an empty function in a fresh bot which will do nothing. You can implement it for custom functionality.
 
<hr>
 
## API Methods

The API methods on this class do not change any of the data you send and the name of the methods are exactly the same as 
 on Telegram's API. The main purpose of implementing them is to be easy to use, by giving you a list of 
 names and their parameters so you can easily make API calls, knowing exactly what parameters this method requires.

Most of them are also equipped with type hints to facilitate developing if you are using a modern IDE.

Each of the API methods return something upon successful or failed requests. If the request is successful, the response will be
 a [Type](../types/README.md) and if it fails, the response will be a JSON object explaining the reason of failure. The Bot class
 will convert this response:

* If the request is successful, it will return the according [Type](../types/README.md) object
* If the request fails, if will return a dict with the key `ok` equal to `False`

### Example
This is an API call using the Bot class which will be successful:
```python
result = bot.sendMessage(chat_id='93856963', text='This is django-tgbot!')
```
In this scenario, the `result` variable will have a [Message](../types/message.md) object since the output of the `sendMessage` method
will be the sent message. You can find the output for each API method in the [Telegram Bot API](https://core.telegram.org/bots/api) or
 you can use the method type hint in this package.

This other API call will fail since the text argument is required for this method:
```python
result = bot.sendMessage(chat_id='93856963')
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
 
## Methods' Arguments

You should have a look at the API documentations while calling methods as they might have certain requirements on some arguments. For example, `parse_mode` argument on some methods
 accepts only from a fixed list of strings and inline keyboards have three optional fields that exactly one of them should be filled with a value.

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


Furthermore, you should also have a look at the accepted type for each argument. Some may only accept int, some may only accept bool, etc..

In some cases, you may need to pass a parameter with the type of one of the predefined Telegram types. 
For example, if you want to send a keyboard along with a message, you need to pass a `ReplyKeyboardMarkup` as the `reply_markup` parameter.
 In these cases, you can either create a JSON object representing the value you want and pass it along or, alternatively,
 you can create the object with the needed type and pass the object itself - it will be then converted to JSON automatically. All of the 
  Telegram types are defined here and you can create objects of those types.
 
Hence, for the example explained above, for sending your keyboard you can create a [ReplyKeyboardMarkup](../types/replykeyboardmarkup.md)
 object pass it through as the `reply_markup` argument. If in some scenario, you need to have the JSON value of an object, all of the
 defined [Type](../types/README.md) in this package have a `to_dict` method to convert that object to a dict object and a `to_json`
 to convert it to JSON.
  
<b>If you want to create a [Type](../types/README.md) object, you should use a method called `a` and not the default constructor.
 For more information please read its [docs](../types/README.md).</b>

### Example

Let's send a keyboard with the sent message in our previous example:

```python
result = bot.sendMessage(

    chat_id='93856963',

    text='This is django-tgbot!'

    reply_markup=ReplyKeyboardMarkup.a([

        [KeyboardButton.a('Left Button'), KeyboardButton.a('Right Button')]

    ])

)
```

