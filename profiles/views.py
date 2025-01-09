from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = RegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)

        if user is not None:
            login(request, user)
            # Перенаправление на параметр next или личный кабинет
            next_url = request.POST.get('next', 'profile')  # Если параметр next отсутствует, редирект на профиль
            return redirect(next_url)
        else:
            messages.error(request, 'Неверный номер телефона или пароль.')

    return render(request, 'login.html')

@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html') 