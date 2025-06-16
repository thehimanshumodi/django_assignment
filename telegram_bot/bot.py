import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.conf import settings
from api.models import CustomUser
from .models import TelegramUser

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    
    # Try to find existing user
    user, created = TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    
    if not created:
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    
    # Try to link with Django user if username matches
    try:
        django_user = CustomUser.objects.get(username=username)
        django_user.telegram_username = username
        django_user.save()
        user.user = django_user
        user.save()
        update.message.reply_text(f'Hello {first_name}! Your Telegram account has been linked to your Django account.')
    except CustomUser.DoesNotExist:
        update.message.reply_text(f'Hello {first_name}! Your Telegram info has been recorded. Please register on our website to link accounts.')

def setup_bot():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set")
    
    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()