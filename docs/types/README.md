# Types

[Telegram Bot API](https://core.telegram.org/bots/api) uses several types for communications with the clients. All of them 
(with regard to the API version mentioned in this doc) are implemented in this package. You can find a complete list of available 
types in the API [here](https://core.telegram.org/bots/api#available-types).

Examples of Types are: Update, Message, User, Chat, etc.

### Constructor
All of the types have their default constructor taking an object holding information about this object. This object can be a dict
or a JSON object. This constructor is designed to load the information from this object, which will be given to it by the Telegram API, 
Bot class and other Types.

If you want to create an object of a Type, you should use the classmethod `a`. All of the Types have this method and they 
accept the exact same arguments as that type Fields (explained later in this document). You can see these arguments either from the
[Telegram Bot API docs](https://core.telegram.org/bots/api#available-types) or from the `fields` attribute of that class.

The `a` method will do some basic validations for the arguments you pass and will return an instance of the Type.

Moreover, some of the more commonly used Types have the `a` method implemented inside their body with type hints in order to make it
easier to use when working with a modern IDE.

### Fields
Each Type has some fields with exact same names as they have in the API docs. The definitions of these fields can be seen
from the `fields` attribute of the class or the API docs. When using the default constructor, the `parse_fields` method will
read these fields from the given object. They will be set as an attribute to the object if and only if they are present in the given object.

Basic validation when you are using the `a` method will use the types given in this attribute, unless you set `validation` equal 
to `False`.

For more commonly used fields of the Types there is a `get_<FIELD_NAME>` method defined which you can use. If the field you
want to use does not have this method you can still access it directly.

For example if you want the message text from an update object you can do:
```python
text = update_obj.get_message().get_text()
```
which will use the `get_message` method of the update object and then the `get_text` method of the message object.

You may, however, want to access the fields like this:
```python
text = update_obj.message.text
```

