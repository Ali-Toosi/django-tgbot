import errno
import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand

from django_tgbot.management import helpers


class Command(BaseCommand):
    help = 'Creates a new Telegram bot'

    def handle(self, *args, **options):

        get_me_result, bot_token = helpers.prompt_token(self)
        bot_name = str(get_me_result.get_first_name())
        bot_username = str(get_me_result.get_username()).lower()

        self.stdout.write('Setting up @{} ...'.format(bot_username))

        helpers.prompt_project_url(self, bot_token, bot_username)

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

        with open(os.path.join(dst, 'credentials.py'), 'w') as f:
            creds_help_text_lines = [
                "# Do not remove these 2 lines:",
                f"BOT_TOKEN = '{bot_token}'  # You should consider using env variables or a secret manager for this.",
                f"APP_NAME = '{bot_username}'"
            ]
            f.write('\n'.join(creds_help_text_lines))

        with open(os.path.join(dst, '__init__.py'), 'w') as f:
            f.write(
                "from . import credentials\n\n\nbot_token = credentials.BOT_TOKEN\napp_name = credentials.APP_NAME\n"
            )

        with open(os.path.join(dst, os.path.join('migrations', '0001_initial.py')), 'r') as f:
            migration = f.read().replace('_BOT_USERNAME', bot_username)
        with open(os.path.join(dst, os.path.join('migrations', '0001_initial.py')), 'w') as f:
            f.write(migration)

        self.stdout.write(self.style.SUCCESS('Successfully created bot {}(@{}).'.format(bot_name, bot_username)))

        self.stdout.write("Next steps:")
        self.stdout.write("\t1. Add '{}' to INSTALLED_APPS in project settings".format(bot_username))
        self.stdout.write("\t2. Add `from {} import urls as {}_urls` to project urls file".format(bot_username, bot_username))
        self.stdout.write("\t3. Add `path('{}/', include({}_urls))` to project urls' urlpatterns".format(bot_username, bot_username))
        self.stdout.write("\t4. `python manage.py migrate`")
        self.stdout.write("Enjoy!")
