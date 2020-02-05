# Update

This object represents the [Update Type](https://core.telegram.org/bots/api#update) in the Bot API.

### Type
An update can have one of several types indicated in the Bot API (e.g. message, channel_post, etc.).

This class has a `type` method that will give you the type of this update. The returned value will be one of the 
available values in the `update_types` module. You can check the type by checking the string values but in order to avoid
errors it is recommended to use the `update_types` module:

```python
from django_tgbot.state_manager import update_types
from django_tgbot.types.update import Update

update: Update = ...

type = update.type()

if type == update_types.Message:
    print('Update is a message')
elif type == update_types.EditedMessage:
    print('Update is an edited message')
elif
    ...
```


These are all of the available update types at the moment:

* **Message**
* **EditedMessage**
* **ChannelPost**
* **EditedChannelPost**
* **InlineQuery**
* **ChosenInlineResult**
* **CallbackQuery**
* **ShippingQuery**
* **PreCheckoutQuery**
* **Poll**
* **PollAnswer**
