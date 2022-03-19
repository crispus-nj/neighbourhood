from ast import Pass
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserAccount

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            return JsonResponse({"User": "invalid user"})
    return render(request, 'accounts/login.html')
    
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')