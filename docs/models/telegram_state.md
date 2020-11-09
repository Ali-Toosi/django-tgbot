# Telegram State
A client can be working with the bot in different settings. For example, a user can send messages to the bot in a private chat or in a group
 or different groups. A bot can send messages visible to our bot in different groups. These should be handled separately. If a user is working
 with the bot in 2 groups at the same time, we do not want their interactions with the bot in one group to interfere with their interactions
 with the bot in the other group or in the private chat. Here comes the **Telegram State**.

## Information stored
**Telegram State** holds information about a client, the chat in which they are using the bot and some other auxiliary data
for helping the bot to handle updates. These auxiliary data are:

* `telegram_user`: The user (either a person or a bot) this state belongs to. This field can be null (will be explained later in this document).
* `telegram_chat`: The chat (private, group, supergroup or channel) this state belongs to. This field can be null (which will be explained later in this document).
* `name`: The state that this client / chat currently has can be named so the bot can recognize it easier. This is basically how the bot
handles the state. It sets a name for the state of this client / chat and it knows what to do when another update comes at a later time. Again,
after processing that update, if it needs to move the user to another state, it will change this name. You can set this name by accessing it directly
or you may use the `set_name` method:
    * `set_name`: Receives a string and sets it as the name.

* `memory`: Basically, it is a JSON object you can store and it will be carried for you whenever a request comes regarding this client / chat.
This memory will always be given to you as a dict and you can send a dict to be stored for you and given to you the next time you want it:
    * `set_memory`: Takes a dict and sets the memory equal to that.
    * `update_memory`: Takes a dict and updates the memory based on that - existing keys will be updates and non-existing keys will be created.
    * `reset_memory`: As the name suggests, resets the memory to empty dict.
    
    
##### Example
Let's say we want to design a bot that takes a user's name and email address in their private chat and prints it. So the Telegram State object
we will be working with, is for this particular user and their private chat with the bot.

1. The name of the state is initially empty. Look at this as a reset state. Now the user sends a message. The bot can accept this
message as a start message and ask for the user's name. Now, it will change the state name to <i>asked_for_name</i>. **The advantage of
having a name for the state is that the next time a message comes from this user in this chat, the bot knows what it was waiting for and hence,
it will realize this new message has to be the user's name.**

2. The next message comes and the bot perceives it as the user's name. Now we want to ask for their email address. However, we shouldn't lose the name.
We can create a new model for this or alter the existing models to store this but it does not make sense to create a new field in the database for
every piece of information we need to keep throughout a simple process. Hence, we use the `memory` of this state. Bot sets the memory as this:

        state.set_memory({
            'name': <Received_Name>
        })
and then asks for the email address. It should also change the state so it knows the next message that comes is the user's email address:

        state.set_name('asked_for_email')

3. Now the user will send another message which contains the email address. It's time to retrieve their name (which we have stored in the memory)
and print it along with the email. We get the name, print it and then reset the state memory and name:

        name = state.get_memory()['name']
        print(...)
        state.reset_memory()
        state.set_name('')
        
This example illustrates the use of state name and state memory. This example is implemented in the demo bot created with this package. You can see it [here](https://github.com/ARKhoshghalb/django-tgbot_demo).


## Possible settings for the user and the chat
As it was mentioned earlier in this doc, the user and the chat in a state can be null. Now we will explain what each of these scenarios mean.

* <b>User: Non-blank, Chat: Non-blank</b>: This is a regular conversation. Like a private chat or a user sending messages to a group.
* <b>User: Non-blank, Chat: Blank</b>: This is when the user is working with the bot in <i>inline mode</i>. Telegram does not send you
information about the chat that user is typing in and you only know the user. For more information please read the Telegram Bot API docs.
* <b>User: Blank, Chat: Non-blank</b>: This is when your bot is a member of a channel and receives updates about that. There is no user sending messages.
It's just the channel and you can define the state on that channel if you want to take actions in the future, with regards to these updates from the channel.
* <b>User: Blank, Chat: Blank</b>: This will never happen. There is always at least one of these two with value.   

    
    
