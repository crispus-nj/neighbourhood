from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'neighbour/index.html')

@login_required(login_url='login')
def landing(request):
    return render(request, 'neighbour/landing.html')