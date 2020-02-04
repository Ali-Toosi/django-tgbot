import errno
import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand

from django_tgbot.bot_api_user import BotAPIUser
from django_tgbot.types.user import User


class Command(BaseCommand):
    help = 'Creates a new telegram bot'

    def handle(self, *args, **options):
        bot_token = input("Enter the bot token (retrieved from BotFather): ")
        api_user = BotAPIUser(bot_token)
        get_me_result = api_user.getMe()
        while type(get_me_result) != User:
            if 'no_connection' not in get_me_result.keys():
                bot_token = input("Bot token is not valid. Please enter again: ")
                api_user.set_token(bot_token)
                get_me_result = api_user.getMe()
            else:
                self.stdout.write(self.style.ERROR("Connection failed. You need to be connected to the internet to run this command."))
                return

        self.stdout.write('Setting up @{} ...'.format(get_me_result.get_username()))

        bot_name = str(get_me_result.get_first_name())
        bot_username = str(get_me_result.get_username()).lower()

        project_url = input("Enter the url of this project to set the webhook (Press Enter to skip): ")
        while len(project_url) > 0 and project_url[-1] == '/':
            project_url = project_url[:-1]
        if project_url != '':
            confirmed = False
            while not confirmed:
                confirmed_text = input("Bot webhook will be set to {}/{}/update/. Do you confirm? (Y/N): ".format(
                    project_url,
                    bot_username
                ))
                confirmed = confirmed_text.lower() in ['yes', 'y']
                if not confirmed:
                    project_url = input("Enter the correct url: ")
                    while len(project_url) > 0 and project_url[-1] == '/':
                        project_url = project_url[:-1]

            res = api_user.setWebhook("{}/{}/update/".format(project_url, bot_username))
            if res['ok']:
                self.stdout.write(self.style.SUCCESS("Webhook was successfully set."))
            else:
                self.stdout.write(self.style.WARNING("Couldn't set webhook:\n{}".format(res['description'])))

        dst = os.path.join(settings.BASE_DIR, bot_username)
        if os.path.isdir(dst):
            self.stdout.write(self.style.ERROR('Directory `{}` already exists.'.format(dst)))
            return

        src = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'bot_template')
        try:
            shutil.copytree(src, dst)
        except OSError as exc:
            if exc.errno == errno.ENOTDIR:
                shutil.copy(src, dst)
            else:
                self.stdout.write(self.style.ERROR("Couldn't copy bot files."))
                return

        with open(os.path.join(dst, '__init__.py'), 'w') as f:
            f.write("# Do not remove these 2 lines:\nbot_token = '{}'\napp_name='{}'".format(bot_token, bot_username))

        self.stdout.write(self.style.SUCCESS('Successfully created bot {}(@{}).'.format(bot_name, bot_username)))

        self.stdout.write("Next steps:")
        self.stdout.write("\t1. Add '{}' to INSTALLED_APPS in project settings".format(bot_username))
        self.stdout.write("\t2. Add `from {} import urls as {}_urls` to project urls file".format(bot_username, bot_username))
        self.stdout.write("\t3. Add `path('{}/', include({}_urls))` to project urls' urlpatterns".format(bot_username, bot_username))
        self.stdout.write("\t4. `python manage.py migrate`")
        self.stdout.write("Enjoy!")
