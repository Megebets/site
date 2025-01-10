from django import forms
from .models import UserProfile
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = UserProfile
        fields = ['phone', 'last_name', 'first_name', 'middle_name', 'password']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_regex = r'^\+7\d{10}$'  # Формат +7XXXXXXXXXX
        if not re.match(phone_regex, phone):
            raise forms.ValidationError("Введите корректный номер телефона (формат +7XXXXXXXXXX).")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data
