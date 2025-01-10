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
            login(request, user)  # Автоматический вход после регистрации
            return redirect('profile')  # Перенаправление на личный кабинет
    else:
        form = RegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})

def login_view(request):
    context = {}
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)

        if user is not None:
            login(request, user)
            # Проверяем параметр next
            next_url = request.POST.get('next') or request.GET.get('next') or '/profiles/profile/'
            return redirect(next_url)
        else:
            context['error_message'] = 'Неверный номер телефона или пароль.'

    return render(request, 'profiles/login.html', context)

@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html') 