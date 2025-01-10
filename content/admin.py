from django.contrib import admin  # Импортируем модуль для управления административной частью сайта
from .models import GalleryImage  # Импортируем модель GalleryImage из текущего приложения

# Регистрируем модель GalleryImage в админ-панели.
# Это позволяет управлять объектами модели через интерфейс Django Admin.
admin.site.register(GalleryImage)
