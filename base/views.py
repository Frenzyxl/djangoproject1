#!/usr/bin/env python3

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'User does not exist')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Incorrect Password')

    context = {}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')
        if password == password_again:
            real_password = password
            user = User.objects.create_user(username=firstname,
                                            email=email,
                                            password=real_password,
                                            first_name=firstname,
                                            last_name=lastname,

                                            )
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Password did not match')

    context = {}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def forgotPassword(request):
    #     if request.method == 'POST':
    #         password = request.POST.get('password')
    #         confirm_password = request.POST.get('password_confirm')
    #
    return render(request, 'password/forgot-password.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
