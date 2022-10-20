"""
ASGI config for webstuhl_back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
import os
from pathlib import Path
import environ 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
environ.Env.read_env(os.path.join(f'{BASE_DIR}\\webstuhl_back\\settings', '.env'))
enviroment = env('ENV')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'webstuhl_back.settings.{enviroment}')

application = get_asgi_application()
