from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .bot import bot
from django_tgbot.types.update import Update


@csrf_exempt
def handle_bot_request(request):
    update = Update(request.body.decode("utf-8"))
    """
    All of the processing will happen in this part. It is wrapped in try-except block
    to make sure the returned HTTP status is 200. Otherwise, if your processors raise Exceptions
    causing this function to raise Exception and not return 200 status code, Telegram will stop
    sending updates to your webhook after a few tries. Instead, take the caught exception and handle it
    or log it to use for debugging later.
    """
    try:
        bot.handle_update(update)
    except Exception:
        pass
    return HttpResponse("OK")
