# Updating your bot's token

Another management command encapsulated in this package is `tgbottoken`. This command allows you to update the token for a bot you have created.

### Step by step guide
1. Open the Django project with `django-tgbot` installed in it
2. Enter this command in the command line (terminal / cmd):  
    
        python manage.py tgbottoken

3. Enter the username for the bot you want to modify (without @):

        > python manage.py tgbottoken
        Enter bot username: <BOT_USERNAME e.g. botdevtestbot>

4. Enter your new API token:  
    
        > python manage.py tgbottoken
        Enter bot username: <BOT_USERNAME e.g. botdevtestbot>
        Enter the bot token (retrieved from BotFather): <YOUR_TOKEN>
    
Your token is updated! If you have set the webhook correctly you can now send messages to your bot and it should respond to the messages.

