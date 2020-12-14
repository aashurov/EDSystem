from django.shortcuts import render, redirect
from .forms import LoginForm, UserUpdateForm,  SetpasswordLogin
from django.contrib.auth import login, logout as ulogout
from .models import UserProfile
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileUpdateForm


def index(request):
    return render(request, 'main/index.html')


def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html', {'form': form})


def ulogin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile = UserProfile.objects.get(user_id=user.id)
            if profile.role == "курер":
                login(request, user)
                return redirect('courier')
            elif profile.role == "менеджер":
                login(request, user)
                return redirect('staff')
            elif profile.role == "клиент":
                login(request, user)
                return redirect('customer')
            else:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'userprofile/login.html', {"form": form})


def logout(request):
    ulogout(request)
    return redirect('index')


def profile(request, user_id):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.userprofile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            redirect('profile', user_id=user_id)
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'userprofile/profile.html', {"u_form": u_form, "p_form": p_form})


def password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetpasswordLogin(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = SetpasswordLogin(request.user)
        return render(request, 'userprofile/password.html', {
            'form': form
        })
    else:
        return redirect('login')