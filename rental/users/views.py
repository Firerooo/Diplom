from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

# Проверка на отсутствие авторизации
def not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(not_logged_in, login_url='/')
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@user_passes_test(not_logged_in, login_url='/') 
def login_view(request):
    next_page = request.GET.get('next', reverse_lazy('listings:home'))  # Получаем next или отправляем на главную

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_page)  # Редирект после входа
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
