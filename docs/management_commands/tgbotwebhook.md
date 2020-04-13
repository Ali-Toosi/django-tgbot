# Updating your bot's webhook

Another management command encapsulated in this package is `tgbotwebhook`. This command allows you to update the webhook address for a bot you have created.

### Step by step guide
1. Open the Django project with `django-tgbot` installed in it
2. Enter this command in the command line (terminal / cmd):  
    
        python manage.py tgbotwebhook

3. Enter the username for the bot you want to modify (without @):

        > python manage.py tgbottoken
        Enter bot username: <BOT_USERNAME e.g. botdevtestbot>

4. You will be asked if you want to change the project URL and use default webhook address or give your own address as webhook.  
<br>
The difference is that if you choose to use the default address, you don't need to change the urls set for you in the project. However, if you choose to provide a customized webhook URL 
you need to take care of the urls' configuration yourself.

5. Enter the URL.
    
Your webhook is updated! If you have set the webhook correctly you can now send messages to your bot and it should respond to the messages.

