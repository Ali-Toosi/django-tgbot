# Processors

<b>To completely understand what processors are, you need to first read the <i>Definitions</i> section from [here](index.md).</b>

Processors are essentially Python functions that take (at least) these 3 named arguments:

* `bot`: The bot instance - should be used for calling API methods. For more information read [Bot class docs](classes/bot.md).
* `update`: The update object received from Telegram. For more information read about [Types](types/README.md) and [Updates](types/update.md).
* `state`: The Telegram State object related to this update. For more information read [Telegram State docs](models/telegram_state.md).


## Creating processors
As explained earlier, processors are just Python functions. So how should we say which functions are processors and which functions are not?

##### Processors module
First of all, processors should be in a place that gets imported to the project at some point. When creating a new bot, a module named `processors.py` is
created. This module will be imported in the code to load all of your processors. You may, however, realize that you are going to have a lot
of processors and it is hard to have them all in one file and thus, you may need to separate them. To do so, you can remove this file and instead,
create a package named `processors` in the same directory. Then put all of your processors in files under this package. <b>Remember! You still need to 
import any file you create, in the `__init__.py` file in root directory of your package.</b> For example:

```
processors
├── __init__.py
├── greetings.py
├── signup.py
└── ...
```

Where `__init__.py` contains:
```
from . import greetings, signup, ...
```

<br>

##### Registering with @processor
Still, not every function you put in these modules will be considered as a processor. You may have a lot of functions, where you want only a few of them
to be processors.

If you want to declare a function as a processor, it should be registered with the `@processor` decorator:
```python
@processor(...args...)
def cool_processor(bot, update, state):
    pass
```

An important note here is that any function you register as a processor should have the 3 named parameters explained above. <b>If you register a processor
that doesnt have at least one of these named parameters it will not be registered and an exception will be raised.</b>

Now let's move on to using this decorator.

## @processor decorator
Each processor checks a few conditions before accepting an update. If those conditions are met then it will process the update. Otherwise, the update will not
be sent to this processor.

These conditions are these four:

1. What is the name of the [state](models/telegram_state.md) related to this update?
2. What is the type of the incoming update? Read more about update types [here](types/update.md)
3. What is the type of the message (if any) in this update? Read more about message types [here](types/message.md)

Then, if the conditions are met, the processor will run. In most cases we want to change the state to something specific if running
of the processor does not face any problems. This automation can be accomplished by the `success` and `fail` arguments:

* `success`: Whatever value this argument has will be set as the name of the state if the processor runs with no <i>problem</i>.
* `fail`: Whatever value this argument has will be set as the name of the state if the faces a <i>problem</i> while running.

In the above definitions, a <i>problem</i> means a `ProcessFailure` exception being raised. So for example, if you receive a 
text message from the user and you find out it is not a valid response from them, you can raise a `ProcessFailure` and their state's name
will change accordingly (it will get the value of `fail` argument).

#### Arguments and descriptions
We saw how a processor works. These are the arguments we can pass to the `@processor` decorator to register a processor:

* **state_manager**: An instance of the state manager will be created with every new bot you create and you can import it from `bot.py`. This object
will be responsible for storing all of the processors and checking their conditions. This is the only required argument.
* **from_states**: This argument is to check the first condition from the list above. It takes a list or a single string and when
a new update arrives, it will check to see if the state name is one of state names accepted by this processor. Special values:
    * If you want to accept updates with all state names, pass **state_types.All**
    * If you want to accept updates with reset states (i.e. empty state names), leave blank or pass an empty string or pass **state_types.Reset**
* **update_types**: This argument is to check the second condition from the list above. It takes a list or a single value and
checks the type of the received update. Use the predefined [update types](types/update.md) to fill this argument. For example, you can pass
`[update_types.Message, update_types.EditedMessage]` to catch messages and edited messages or `update_types.ChannelPost` to get only channel posts.
Special values:
    * If you want to accept all update types, leave this argument blank
* **exclude_update_types**: This argument is also for checking the second condition. The only difference with `update_types` is that here
you provide the update types you do NOT want to accept. Follows the same logic and values.
* **message_types**: This argument is for checking the third condition in the list above. It only works if the received update contains
a message. It takes a list or a single value and checks the type of the message in the update. Use the predefined [message types](types/message.md) for
this argument. For example you can pass `[message_types.Voice, message_types.Audio]` to only catch messages containing an audio file. Special values:
    * If you want to accept all message types, leave this argument blank
* **exclude_message_types**: This argument is also for checking the third condition. The only difference with `message_types` is that here
you provide the message types you do NOT want to accept. Follows the same logic and values.
* **success**: The value you want the state name to get in case the processor runs successfully. Special values:
    * If you don't want the state to be affected by this and want to change it manually yourself, leave it blank.
    * If you want to reset the state (to become empty), pass `state_types.Reset`.
    * If you want to keep the current state, pass `state_types.Keep`. Please note that this is different than leaving it as blank.
    When using this, no matter what changes you manually perform on the state name, after the processor is run the state name will
    become whatever it was before running the processor.
* **fail**: The value you want the state name to get in case the processor raises `ProcessFailure`. Special values:
    * Exactly like the `success`.
    
These are 2 examples of processors registered with `@processor`:
```python
@processor(
    state_manager, from_states='asked_for_name', 
    update_types=[update_types.Message, update_types.EditedMessage], 
    message_types=message_types.Text, 
    success='asked_for_email', fail=state_types.Keep
)
def get_name(bot, update, state):
    pass
```

```python
@processor(
    state_manager, from_states=['asked_for_media', 'asked_for_file'], 
    update_types=update_types.Message, 
    exclude_message_types=[message_types.Text, message_types.PinnedMessage], 
    success=state_types.Reset, fail=state_types.Keep
)
def get_anything_but_text(bot, update, state):
    pass
``` 



