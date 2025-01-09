from django.urls import path
from .views import register, profile_view
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', profile_view, name='profile'),
] 
  