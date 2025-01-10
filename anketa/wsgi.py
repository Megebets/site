"""
WSGI config for anketa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os  # Импортируем модуль os для работы с операционной системой и переменными окружения

from django.core.wsgi import get_wsgi_application  # Импортируем функцию для получения WSGI-приложения

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE.
# Эта переменная указывает, какой файл настроек использовать для проекта Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anketa.settings')

# Создаём объект WSGI-приложения. Этот объект будет использоваться сервером WSGI
# (например, Gunicorn или uWSGI) для обработки HTTP-запросов.
application = get_wsgi_application()
