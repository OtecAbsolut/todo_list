from django.shortcuts import render, redirect, reverse
from registration.forms import CustomUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def create_user(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)
        success_url = reverse('registration:login')

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    """ Логин """
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """ Вьюха разлогирования """
    logout(request)
    success_url = reverse('registration:login')
    return redirect(success_url)
