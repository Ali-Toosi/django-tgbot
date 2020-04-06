from django_tgbot.bot_api_user import BotAPIUser
from django_tgbot.types.user import User


def validate_token(bot_token):
    """
    If False, the second returned value is:
        0 if token is not valid
        1 if internet connection is not established
    If True, the second argument will be getMe result
    """
    api_user = BotAPIUser(bot_token)
    get_me_result = api_user.getMe()
    if type(get_me_result) != User:
        if 'no_connection' not in get_me_result.keys():
            return False, 0
        else:
            return False, 1
    return True, get_me_result


def prompt_token(command_line, prompt_message='Enter the bot token (retrieved from BotFather): '):
    """
    Returns either None or getMe result
    """
    bot_token = input(prompt_message)
    validation = validate_token(bot_token)
    while not validation[0]:
        if validation[1] == 0:
            bot_token = input("Bot token is not valid. Please enter again: ")
            validation = validate_token(bot_token)
        elif validation[1] == 1:
            command_line.stdout.write(
                command_line.style.ERROR(
                    "Connection failed. You need to be connected to the internet to run this command."
                )
            )
            return None, bot_token
    return validation[1], bot_token


def set_webhook(bot_token, url):
    api_user = BotAPIUser(bot_token)
    res = api_user.setWebhook(url)
    return res


def prompt_webhook(command_line, bot_token, bot_username):
    webhook_url = input("Enter the url to be set as webhook for @{}: ".format(bot_username))
    res = set_webhook(bot_token, webhook_url)
    if res['ok']:
        command_line.stdout.write(command_line.style.SUCCESS("Successfully set webhook."))
    else:
        command_line.stdout.write(command_line.style.WARNING("Couldn't set webhook:\n{}".format(res['description'])))


def prompt_project_url(command_line, bot_token, bot_username):
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

        res = set_webhook(bot_token, "{}/{}/update/".format(project_url, bot_username))
        if res['ok']:
            command_line.stdout.write(command_line.style.SUCCESS("Successfully set webhook."))
        else:
            command_line.stdout.write(command_line.style.WARNING("Couldn't set webhook:\n{}".format(res['description'])))
