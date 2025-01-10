"""
ASGI config for anketa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os  # Импорт модуля os для работы с операционной системой и переменными окружения

from django.core.asgi import get_asgi_application  # Импорт функции для получения объекта ASGI-приложения

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE,
# которая указывает Django, где искать файл настроек проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anketa.settings')

# Создаём объект ASGI-приложения. Этот объект будет использоваться сервером ASGI
# (например, Daphne или Uvicorn) для обработки запросов.
application = get_asgi_application()
