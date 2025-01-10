from django.apps import AppConfig  # Импортируем базовый класс для конфигурации приложения

# Определяем класс конфигурации для приложения `content`
class ContentConfig(AppConfig):
    # Устанавливаем тип поля по умолчанию для автоинкрементных ключей в модели
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Указываем имя приложения
    name = 'content'
