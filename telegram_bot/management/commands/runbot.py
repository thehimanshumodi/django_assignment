from django.core.management.base import BaseCommand
from telegram_bot.bot import setup_bot

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        setup_bot()