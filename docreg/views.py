from django.shortcuts import render

# Create your views here.


def docreg(request):
    return render(request, 'doctor_signup.html')
