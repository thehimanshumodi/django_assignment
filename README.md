# Django Project with DRF, Celery, and Telegram Bot

This project is a small Django application designed to demonstrate backend development skills. It integrates Django REST Framework (DRF), user authentication, Celery for asynchronous tasks, and a Telegram bot for user interaction and data storage.

## Features

* **Django Project Setup**: Standard Django project structure with `settings.py` configured for production-like environments, using environment variables for sensitive data.
* **Django REST Framework (DRF)**: Implements RESTful APIs.
* **Authentication**: Django's session authentication for web-based access (Admin, browsable API) and DRF Token Authentication (via Djoser) for API access.
* **Celery Integration**: Configured with Redis as a message broker, demonstrating a background task (sending a welcome email after user registration).
* **Telegram Bot Integration**: Collects Telegram user information (`user_id`, `username`, `first_name`, `last_name`) when a user sends the `/start` command, storing it in a Django database model.
* **Code Management**: Clean, well-documented code with a detailed `README.md`. (Proper commit history is assumed to be managed during development).

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* **Python 3.8+**
* **pip** (Python package installer)
* **Redis Server**: Ensure Redis is installed and running, as it's used by Celery.
    * **macOS (Homebrew)**: `brew install redis && brew services start redis`
    * **Linux (apt)**: `sudo apt update && sudo apt install redis-server && sudo systemctl start redis-server`
    * **Windows**: Download from [Redis website](https://redis.io/download/) or use WSL.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd django_assignment # Or whatever your project folder is named
    ```
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows (Command Prompt):
    venv\Scripts\activate.bat
    # On Windows (PowerShell):
    venv\Scripts\Activate.ps1
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1.  **Apply database migrations**:
    ```bash
    python manage.py makemigrations myapp
    python manage.py migrate
    ```
2.  **Create a superuser** (for Django Admin access):
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up your admin credentials.

## Environment Variables

The project uses a `.env` file (based on `.env.example`) to manage sensitive configurations and settings. Create a file named `.env` in the root of your project and populate it as follows:

```ini
# Rename this file to .env and fill in your actual values

# Django Settings
DJANGO_SECRET_KEY='your_very_secret_and_long_key_here_at_least_50_chars'
DJANGO_DEBUG='True' # Set to False for production deployments
DJANGO_ALLOWED_HOSTS='127.0.0.1,localhost' # Add your production domain(s) here
DJANGO_CSRF_TRUSTED_ORIGINS='[http://127.0.0.1](http://127.0.0.1),http://localhost' # Add your production URL(s) here

# Celery and Redis Settings
CELERY_BROKER_URL='redis://localhost:6379/0'
CELERY_RESULT_BACKEND='redis://localhost:6379/0'

# Email Settings (for send_welcome_email_task - currently uses console backend for testing)
# For production, uncomment and configure with your SMTP details (e.g., Mailgun, SendGrid):
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST='smtp.example.com'
# EMAIL_PORT='587'
# EMAIL_USE_TLS='True'
# EMAIL_HOST_USER='your_email@example.com'
# EMAIL_HOST_PASSWORD='your_email_password'
# DEFAULT_FROM_EMAIL='noreply@your-domain.com'

# Telegram Bot Settings
TELEGRAM_BOT_TOKEN='YOUR_TELEGRAM_BOT_TOKEN' # <-- **REQUIRED: Get this from BotFather**
