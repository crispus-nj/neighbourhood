from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Business, Location, Post
from .forms import BusinessRegistrationForm

def home(request):
    return render(request, 'neighbour/index.html')

@login_required(login_url='login')
def landing(request):
    return render(request, 'neighbour/landing.html')

@login_required(login_url='login')
def business(request):
    businesses = Business.objects.all()
    form = BusinessRegistrationForm()
    context = {'businesses': businesses, 'form':form}

    return render(request, 'neighbour/business.html', context)
