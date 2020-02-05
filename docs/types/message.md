# Message

This object represents the [Message Type](https://core.telegram.org/bots/api#message) in the Bot API.

### Type
Each message has a type. For example, it can be a text message, a picture or successful payment. To see a full list of 
message types check the `message_types` module from `django_tgbot.state_manager.message_types`.

This class has a `type` method that will give you the type of this message. The returned value will be one of the 
available values in the `message_types` module. You can check the type by checking the string values but in order to avoid
errors it is recommended to use the `message_types` module:

```python
from django_tgbot.state_manager import message_types
from django_tgbot.types.message import Message

message: Message = ...

type = message.type()

if type == message_types.Game:
    print('Message is a Game!')
elif type == message_types.Location:
    print('Message is a location')
elif
    ...
```

These are all of the available message types at the moment:

* **Text **
* **Audio **
* **Document **
* **Animation **
* **Game **
* **Photo **
* **Sticker **
* **Video **
* **Voice **
* **VideoNote **
* **Contact **
* **Location **
* **Venue **
* **Poll **
* **NewChatMembers **
* **LeftChatMembers **
* **NewChatTitle **
* **NewChatPhoto **
* **DeleteChatPhoto **
* **GroupChatCreated **
* **SupergroupChatCreated **
* **ChannelChatCreated **
* **MigrateToChatId **
* **MigrateFromChatId **
* **PinnedMessage **
* **Invoice **
* **SuccessfulPayment **
* **PassportData **