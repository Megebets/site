"""
URL configuration for anketa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Импортируем модуль для админ-панели Django
from django.urls import path, include  # Импортируем функции для маршрутизации (path) и подключения других маршрутов (include)
from django.views.generic import TemplateView  # Импортируем базовый класс представления для отображения шаблона

# Список маршрутов для проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для админ-панели, доступен по адресу /admin/
    
    # Подключаем маршруты из приложения profiles. Все URL с префиксом /api/ будут обрабатываться в profiles.urls.
    path('api/', include('profiles.urls')),  
    
    # Маршрут для главной страницы. Используется TemplateView, который просто отображает шаблон main/main.html.
    path('', TemplateView.as_view(template_name='main/main.html'), name='home'),
]
