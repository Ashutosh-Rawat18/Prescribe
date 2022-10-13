from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'loginchoice.html')


def register(request):
    return render(request, 'signup_page.html')


def docreg(request):
    return render(request, 'doctor_signup.html')


def patreg(request):
    return render(request, 'patient_signup.html')
