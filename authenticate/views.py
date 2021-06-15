from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib import auth

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'SignInUp.html')

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password2 = request.POST['password2']
        context = {
            'fieldValues': request.POST,
        }
        if username and password:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if len(password) < 8:
                        messages.error(
                            request, 'Password must be atleast 8 characters.')
                        return render(request, 'SignInUp.html', context)
                    else:
                        user = User.objects.create_user(
                            username=username, email=email)
                        user.set_password(password)
                        user.is_active = True
                        user.save()
                        messages.success(
                            request, 'You are successfully registered with us. Now login to use tools.')
                        return render(request, 'SignInUp.html')
                else:
                    messages.error(
                        request, 'This EmailID is in use. Please use another EmailID')
                    return render(request, 'SignInUp.html')
            else:
                messages.error(
                    request, 'This username is already taken. Please use other username.')
                return render(request, 'SignInUp.html')
        else:
            messages.error(request, 'Please fill all fields!')
            return render(request, 'SignInUp.html')


def login(request):
    if request.method == "GET":
        return render(request, 'SignInUp.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username + '! You are now logged in.')
                    return redirect('operateotext:tools')
                else:
                    messages.error(
                        request, 'Your account is not activated. Please check your email for verification link.')
                    return render(request, 'SignInUp.html')
            else:
                messages.error(
                    request, 'Invalid Credentials! Please try again.')
                return render(request, 'SignInUp.html')
        else:
            messages.error(request, 'Please fill all fields!')
            return render(request, 'SignInUp.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You have been logged out!')
        return redirect('operateotext:index')
