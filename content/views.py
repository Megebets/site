from django.shortcuts import render  # Импорт функции для рендера HTML-страниц с контекстом
from .models import GalleryImage  # Импорт модели GalleryImage для работы с изображениями из базы данных

# Представление для отображения галереи изображений
def gallery(request):
    # Извлекаем все объекты модели GalleryImage из базы данных
    images = GalleryImage.objects.all()
    
    # Отправляем запрос, HTML-шаблон 'main/main.html', и контекст с ключом 'images', содержащим список изображений
    return render(request, 'main/main.html', {'images': images})
