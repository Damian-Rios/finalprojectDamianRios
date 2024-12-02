from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# add to dashboard view when created
# will need to add @login_required(login_url='login')
# from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('portfolio:dashboard'))
    return render(request, 'users/index.html')


def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

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
    return redirect('login')