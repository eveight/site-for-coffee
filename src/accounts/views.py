from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_username = request.POST['username']
            user_password = request.POST['password']
            user = authenticate(request, username=user_username, password=user_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')
    return render(request, 'accounts/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    return render(request, 'accounts/register.html', {'register_form': register_form})
