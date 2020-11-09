from django_tgbot.bot_api_user import BotAPIUser
from django_tgbot.types.update import Update


class AbstractTelegramBot(BotAPIUser):
    def __init__(self, token, state_manager):
        super(AbstractTelegramBot, self).__init__(token)
        self.state_manager = state_manager

    def handle_update(self, update: Update):
        user = update.get_user()
        chat = update.get_chat()

        if user is not None:
            db_user = self.get_db_user(user.get_id())
        else:
            db_user = None

        if chat is not None:
            db_chat = self.get_db_chat(chat.get_id())
        else:
            db_chat = None

        db_state = self.get_db_state(db_user, db_chat)

        self.pre_processing(
            update,
            chat=chat,
            db_chat=db_chat,
            user=user,
            db_user=db_user,
            state=db_state
        )

        processors = self.state_manager.get_processors(update, db_state)

        for processor in processors:
            processor(self, update, db_state)

        self.post_processing(
            update,
            chat=chat,
            db_chat=db_chat,
            user=user,
            db_user=db_user,
            state=db_state
        )

    def poll_updates_and_handle(self):
        updates = self.getUpdates()
        offset = None
        total_count = 0
        while len(updates) > 0:
            total_count += len(updates)
            for update_json in updates:
                update = Update(update_json)
                self.handle_update(update)
                offset = int(update.get_update_id()) + 1
            updates = self.getUpdates(offset=offset)
        return total_count

    def pre_processing(self, update: Update, user, db_user, chat, db_chat, state):
        if db_user is not None:
            db_user.first_name = user.get_first_name()
            db_user.last_name = user.get_last_name()
            db_user.username = user.get_username()
            db_user.save()

        if db_chat is not None:
            db_chat.type = chat.get_type()
            db_chat.username = chat.get_username()
            db_chat.title = chat.get_title()
            db_chat.save()

    def post_processing(self, update: Update, user, db_user, chat, db_chat, state):
        pass

    def get_db_user(self, telegram_id):
        """
        Should be implemented - Creates or retrieves the user object from database
        :param telegram_id: The telegram user's id
        :return: User object from database
        """
        pass

    def get_db_chat(self, telegram_id):
        """
        Should be implemented - Creates or retrieves the chat object from database
        :param telegram_id: The telegram chat's id
        :return: Chat object from database
        """
        pass

    def get_db_state(self, db_user, db_chat):
        """
        Should be implemented - Creates or retrieves a state object in the database for this user and chat
        :param db_user: The user creating this state for
        :param db_chat: The related chat
        :return: a state object from database
        """
        pass
