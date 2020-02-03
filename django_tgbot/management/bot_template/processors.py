from django_tgbot.decorators import bot_state
from .bot import state_manager


@bot_state(state_manager, waiting_for='*')
def hello_world(bot, update, state):
    bot.sendMessage(update.get_chat().get_id(), 'Hello!')
