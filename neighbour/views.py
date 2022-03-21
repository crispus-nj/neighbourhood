from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Business, Location, Post
from .forms import BusinessRegistrationForm
from accounts.models import Profile, UserAccount

def home(request):
    if request.user.is_authenticated: 
        return redirect('landing')
    return render(request, 'neighbour/index.html')

@login_required(login_url='login')
def landing(request):
    user = UserAccount.objects.get(id = request.user.id)
    bizna = Business.objects.all()
    prof = user.users.all()
    for profile in prof:
        crispus = Location.objects.get(id = profile.location.id)
        biashara = crispus.business.all()
        print(biashara)
        bizna = biashara
    location = user.people.all()
    locations = Location.objects.all()
    context = {'location': location, 'bizna':bizna, 'locations': locations}
    return render(request, 'neighbour/landing.html', context)

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
