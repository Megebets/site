from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    username = None  # Отключаем стандартное поле username
    phone = models.CharField(max_length=15, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)

    # Указываем уникальные related_name
    groups = models.ManyToManyField(
        Group,
        related_name="userprofile_groups",  # Уникальное имя для обратной связи
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="userprofile_permissions",  # Уникальное имя для обратной связи
        blank=True,
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name']
