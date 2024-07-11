from django.shortcuts import render, redirect

from .forms import RegisterForm;
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            messages.success(request, "Signup Successfully")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                raw_password = form.cleaned_data['password']
                user = authenticate(username=username, password=raw_password) 
                if user is not None: 
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return redirect('profile')
        
        else: 
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')
    



def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login') 

def user_logout(request):
    logout(request)
    messages.warning(request, "Logged Out Successfully")
    return redirect('login')

def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Your password was successfully updated!")
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'password_change.html', {'form': form})   
    else:
        messages.error(request, "You need to log in to change your password.")
        return redirect('login')

def password_change_simple(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Your password was successfully updated!")
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'password_change_simple.html', {'form': form})
    else:
        messages.error(request, "You need to log in to change your password.")
        return redirect('login')
