from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'contact_phone', 'has_parents')  # Укажите нужные поля
    actions = ['reset_password']

    def reset_password(self, request, queryset):
        for user in queryset:
            user.set_password('new_password')  # Укажите желаемый пароль
            user.save()
        self.message_user(request, "Пароли были успешно сброшены.")
    reset_password.short_description = "Сбросить пароль пользователей"

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
