from django.apps import AppConfig

class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self):
        if not hasattr(self, 'already_run'):
            from .bot import setup_bot
            import threading
            
            # Run bot in a separate thread
            bot_thread = threading.Thread(target=setup_bot, daemon=True)
            bot_thread.start()
            
            self.already_run = True