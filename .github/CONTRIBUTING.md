# Contributing to the package

Thank you for your interest in making this package better for everyone!

Please open your PRs to the **dev** branch. If you have your own ideas for improvement that's awesome go for it. If not,
here's a list of features requested by people throughout the time that you could work on (in the order of priority):
- A `processor` should be able to terminate the processing flow - meaning that it could prevent other processors from being run.
This is particularly useful for when you want to handle exception cases and you don't want to have the exception scenario being checked in every processor.
E.g. you want to cancel whatever process the user is undertaking if they enter `/cancel` - no more processors should run.
- Catch up with Telegram API changes (we are currently upto V4.9, [Telegram's changelog](https://core.telegram.org/bots/api-changelog) could be used to see what features
    have been added ever since.)
- Examples are a great way for people to quickly get the idea of how the package works and create more bots. I have 
    created a few example bots in a separate repo, if you have developed bots (or are willing to do so, maybe as part of
    your acquaintance process with the package) please add them to that repo so other people could learn faster. This is the demo
    repo: https://github.com/Ali-Toosi/django-tgbot_demo
- An additional filter could be implemented on `processor`s to allow only certain chats (i.e. certain Telegram ids) to enter a processor.
- Add a dictionary of words for predefined texts (so instead of writing your own message to be sent in each processor,
    create a list of them somewhere else and only refer to them whenever needed). This helps a lot with changing your bot's messages
    without needing to go too deep inside the code. (Could potentially use something like Django's translation system as well.)
- Create a dictionary of emojis so the developer doesn't have to copy paste it from somewhere else inside the code but just
    refer to them with their code/slug.
- Add some automated tests to the package so we can make proceed with more contributions more confidently. (There are 0 
    automated tests in the code right now so no matter how many you add it would be a great contribution.)
- Descriptions of the manage.py commands for setting the bot web-hook are not completely clear to everyone.
- Project docs only scratch the surface of all the things that could be done and don't cover everything. If you have worked with the package for some time and
    have found areas not covered in the docs, that would be great to write up something for them.
- As of now, the bot only processes user's requests and answers them. A mechanism for sending messages to all users or a group
    of users who have used the bot in the past would be cool. Read this issue for more context and also a suggestion of how it can
    be implemented. ([related issue](https://github.com/Ali-Toosi/django-tgbot_demo/issues/2))
- Although "commands" are basically text messages that start with `/`, some sort of special support for them could be added.
([related issue](https://github.com/Ali-Toosi/django-tgbot/issues/9))
 
 You could also join our Telegram group to have a discussion about these: https://t.me/DjangoTGBotChat
