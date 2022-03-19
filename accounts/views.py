from ast import Pass
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserAccount
from .forms import RegistrationForm

# Create your views here.
def register(request):
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
            user.is_active = True
            user.save()
            login(request, user)

            return redirect('home')
        else :
            render(request, 'accounts/register.html', {'form': form})
    else :
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_user(request):
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