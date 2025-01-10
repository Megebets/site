from django.db import models  # Импортируем модуль для работы с моделями в Django

# Определяем модель GalleryImage, которая используется для хранения изображений в галерее
class GalleryImage(models.Model):
    # Поле для названия изображения
    title = models.CharField(max_length=100)
    # Поле для загрузки изображений. Файлы будут сохраняться в папке 'gallery/'.
    image = models.ImageField(upload_to='gallery/')
    # Поле с датой и временем загрузки изображения. Значение устанавливается автоматически при создании объекта.
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Метод __str__ возвращает строковое представление объекта. Здесь это название изображения.
    def __str__(self):
        return self.title
