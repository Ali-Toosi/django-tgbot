from django.core.management.base import BaseCommand

from django_tgbot.management import helpers


class Command(BaseCommand):
    help = 'Updates the webhook address for a Telegram Bot'

    def handle(self, *args, **options):
        get_me_result, bot_token = helpers.prompt_token(self)
        bot_name = str(get_me_result.get_first_name())
        bot_username = str(get_me_result.get_username()).lower()

        self.stdout.write(f"\nChanging the webhook for {bot_name} (@{bot_username})")

        again = True
        while again:
            choice = input("Please choose from the options:\n"
                           " 1. Set the project URL and use default webhooks\n"
                           " 2. Set a custom webhook address for this bot\n")
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
