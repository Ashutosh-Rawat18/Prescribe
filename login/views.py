from django.shortcuts import redirect, render
from django.contrib import auth
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

# def login(request):
#     return render(request, 'loginchoice.html')


# Create your views here.


def login(request):
    if request.method == 'POST':
        username1 = request. POST['lUsername']
        password1 = request. POST['lpassword']

        x = auth.authenticate(username=username1, password=password1)

        if x is not None:
            auth.login(request, x)

            return redirect('home')
        else:

            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def lreg(request):
    return redirect('register page')


def register(request):
    return render(request, 'signup_page.html')


def home(request):
    return render(request, 'doctor_signup.html')
