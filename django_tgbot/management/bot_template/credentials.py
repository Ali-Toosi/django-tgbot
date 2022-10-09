"""
BOT_TOKEN can contain more than one bot. If so, there will be a separate URL created for each bot
and each bot will respond separately. However, they will still be using the same database. If you need
to handle business logic separately for different bots, the bot username for this request is passed to
the processor.
A good use case of multi-bot per code feature is for testing your bots. You may have two different
bots set up in the code, one your actual production bot with proper webhooks and the other would be
your test bot which you would host on your local.
"""

# Consider using env variables or a secret manager for storing your bot tokens.
# Also be mindful that the bot token will be present in the webhook URL. If your incoming requests are
# logged somewhere with the accessed URL, the token could be visible from those logs.
