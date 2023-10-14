# views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .models import CustomUser  


def default_view(request):
    return render(request,'accounts/index.html')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create and save the user to the database
            user = form.save()
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            

            try:
                
                user = CustomUser.objects.get(email=email)
                if user.password==password:
                    

                    # Credentials are valid
                    request.session['user_id'] = user.first_name  # Create a user session
                    return redirect('index')  # Redirect to the desired page
                else:
                    messages.error(request, "Invalid email or password. Please try again.")
            except CustomUser.DoesNotExist:
                messages.error(request, "Invalid email or password. Please try again.")
        else:
            messages.error(request, "Invalid form data. Please try again.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')
