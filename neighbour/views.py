from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Business, Location, Post

def home(request):
    return render(request, 'neighbour/index.html')

@login_required(login_url='login')
def landing(request):
    return render(request, 'neighbour/landing.html')

@login_required(login_url='login')
def business(request):
    businesses = Business.objects.all()

    context = {'businesses': businesses}

    return render(request, 'neighbour/business.html', context)
