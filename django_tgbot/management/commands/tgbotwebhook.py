import os

from django.conf import settings
from django.core.management.base import BaseCommand

from django_tgbot.management import helpers

import importlib.util


class Command(BaseCommand):
    help = 'Updates the webhook for an existing tgbot'

    def handle(self, *args, **options):
        bot_username = input('Enter the username of the bot (without @): ').lower()
        dst = os.path.join(settings.BASE_DIR, bot_username)
        init_file = os.path.join(dst, 'credentials.py')

        if not os.path.isfile(init_file):
            self.stdout.write(
                self.style.ERROR('No such bot found. Make sure you have created your bot with command `createtgbot`.')
            )
            return

        # spec = importlib.util.spec_from_file_location("__init__", init_file)
        spec = importlib.util.spec_from_file_location("credentials", init_file)
        init_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(init_module)

        bot_token = init_module.BOT_TOKEN

        again = True
        while again:
            choice = input("Please choose from the options:\n"
                           " 1. I want to change the project URL and use default webhooks\n"
                           " 2. I want to set a custom webhook URL for this bot\n")
            try:
                if int(choice) == 1:
                    helpers.prompt_project_url(self, bot_token, bot_username)
                    again = False
                elif int(choice) == 2:
                    helpers.prompt_webhook(self, bot_token, bot_username)
                    again = False
                else:
                    self.stdout.write('Did not recognize choice. Try again: ')
                    again = True
            except ValueError:
                self.stdout.write('Respond only with the number of your selected option: ')
                again = True
