# ReplyKeyboardMarkup
This object is used to create and send keyboards to Telegram as reply markups with the messages.

Like other Type objects, this should be created using the `a` method. Note that the `keyboard` argument should be an array of
array of `KeyboardButton`s.

This is an example of a valid reply keyboard created:

```python
keyboard = ReplyKeyboardMarkup.a(keyboard=[
    [KeyboardButton.a(text='Button A'), KeyboardButton.a(text='Button B')],
    [KeyboardButton.a(text='Button C', request_location=True)]
], resize_keyboard=True)
```