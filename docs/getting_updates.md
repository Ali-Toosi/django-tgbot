# Getting Updates
<br>
There are 2 ways you can get updates from Telegram API: Webhooks and Polling.

### Webhook
In order to use webhooks for getting updates from Telegram API, you need to have your project
running and accessible with a public address. If you have not yet deployed your project publicly and it is
only running on localhost, you can still use [Ngrok](http://ngrok.com) to make your local run accessible publicly.

If you have followed the steps explained in the setup, all you need to do in order to create the webhook
is to provide the public address your bot is running on (either your public host or Ngrok).

You will be asked to provide this address once you are setting up your bot. If you have skipped that part
or you are changing the address, you can still use manage.py commands to set the webhook address.

Open a terminal and write command:
```plain
python3 manage.py tgbotwebhook
```

You will be asked to enter your bot's username. After you enter the username you will be asked about
whether you are going to provide the project address (so the webhook will be set accordingly automatically) or
you would like to enter the custom address yourself.

The last step is to just enter the address (either the project address or your custom webhook address) and the webhook
will be set.

### Polling
<i>Please note that this is still not suitable to be used in production and should only be used for local testing purposes.</i>

You can also choose not to use webhooks and instead, load the updates yourself whenever you need them.
In order to do that, all you need to do is run the project (`python3 manage.py runserver`) then open this address in your browser:
```plain
127.0.0.1:8000/[BOT_USERNAME]/poll/
```
Note that you should replace `8000` with the port you are using and `[BOT_USERNAME]` with your bot's username.

This will fetch all of the pending updates from Telegram API and handle them. It will then print on the screen
the number of updates that were handled. Whenever you want to handle new waiting updates, refresh the page.