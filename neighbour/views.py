from django.shortcuts import redirect, render
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

    if request.method == 'POST':
        form = BusinessRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            location = form.cleaned_data['location']
            user = request.user

            print(name, category, image, location, user)

            business = Business.objects.create(
                name = name,
                category = category,
                image = image,
                location = location,
                user = user
            )
            business.save()

            return redirect('business')


    form = BusinessRegistrationForm()
    context = {'businesses': businesses, 'form':form}

    return render(request, 'neighbour/business.html', context)
