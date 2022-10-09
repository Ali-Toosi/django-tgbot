from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django_tgbot.types.update import Update

from .bot import bots

import logging


@csrf_exempt
def handle_bot_request(request, token):
    update = Update(request.body.decode("utf-8"))
    """
    All of the processing will happen in this part. It is wrapped in a try-except block
    to make sure the returned HTTP status is 200. Otherwise, if your processors raise Exceptions
    causing this function to break and not return 200 status code, Telegram will stop
    sending updates to your webhook after a few tries. The exception (if any) is caught for you to handle it
    or log it to use for debugging later.
    """
    try:
        bot = bots[token]
    except KeyError:
        return HttpResponse("Not found.", status=404)

    try:
        bot.handle_update(update)
    except Exception as e:
        if settings.DEBUG:
            raise e
        else:
            logging.exception(e)
    return HttpResponse("OK")


def poll_updates(request, token):
    """
    Polls all waiting updates from the server. Note that webhook should not be set if polling is used.
    You can delete the webhook by passing an empty URL as the address.
    """
    try:
        bot = bots[token]
    except KeyError:
        return HttpResponse("Not found.", status=404)

    count = bot.poll_updates_and_handle()
    return HttpResponse(f"Processed {count} update{'' if count == 1 else 's'}.")
