from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
"""
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('portfolio:dashboard'))
    return render(request, 'users/index.html')
"""

def landing(request):
    if request.user.is_authenticated:
        return redirect(reverse('portfolio:dashboard'))
    return render(request, 'users/landing_page.html')


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users:login')

    context = {'registerForm': form}
    return render(request, 'users/register.html', context=context)


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('portfolio:dashboard')

    context = {'loginForm': form}
    return render(request, 'users/login.html', context=context)


def logout_view(request):
    auth.logout(request)
    return redirect('users:login')
