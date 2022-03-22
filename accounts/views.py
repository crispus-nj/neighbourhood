from ast import Pass
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from neighbour.models import Business, Location

from .models import Profile, UserAccount
from .forms import RegistrationForm, ProfileCreationForm

# Create your views here.
def register(request):
    if request.user.is_authenticated: 
        return redirect('landing')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            username = email.split("@")[0]

            user = UserAccount.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password
            )
            user.phone_number = phone_number
            location = Location.objects.create(
                name = "Kenya"
            )
            # location.people.set(user)
            profile = Profile.objects.create(
                user = user,
                location = location
            )
            profile.save()
            user.is_active = True
            user.save()

            
            login(request, user)

            return redirect('landing')
        else :
            render(request, 'accounts/register.html', {'form': form})
    else :
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_user(request):
    if request.user.is_authenticated: 
        return redirect('landing')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else :
            return JsonResponse({"User": "invalid user"})
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def user_profile(request, pk):
    user = UserAccount.objects.get(id = pk)
    prof = Profile.objects.get(id = pk)
    profile = user.users.all()
    business = user.author.all()
    form = ProfileCreationForm()
    context = {'form': form, 'profile': profile, 'prof':prof, 'business': business}

    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def edit_user(request):
    user = request.user
    prof = Profile.objects.get(id = request.user.id)
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST, request.FILES, instance=prof)
        print(form.errors)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            bio = form.cleaned_data['bio']
            location = form.cleaned_data['location']
            user = request.user

            user = Profile.objects.create(
                avatar = avatar,
                bio = bio,
                location = location,
                user = user
            )
            return redirect('profile', request.user.id)
        else :
            return JsonResponse({"invalid form": "user"})

    form = ProfileCreationForm(instance=prof)
    context = {'form': form, 'prof': prof}
    return render(request, 'accounts/edit_profile.html', context)