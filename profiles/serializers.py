from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        extra_kwargs = {
            "user": {"required": False},  # Поле user не обязательно при отправке
        }

    def create(self, validated_data):
        # Удаляем user из validated_data, если он уже передан вручную
        user = validated_data.pop("user", None)

        # Создаем профиль, передавая user отдельно
        return UserProfile.objects.create(user=user, **validated_data)
