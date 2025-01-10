from content.views import gallery  # Импортируем представление `gallery` из приложения `content`

# Определяем маршруты для приложения
urlpatterns = [
    # Маршрут для главной страницы.
    # URL-адрес '/' будет обрабатываться представлением `gallery`, и этот маршрут будет иметь имя 'home'.
    path('', gallery, name='home'),
]
