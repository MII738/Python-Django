from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not found. Please sign up.")
            return redirect('signup')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('shopping')
        else:
            messages.error(request, "Incorrect password. Please try again.")
            return render(request, 'accounts/login.html', {'username': username})

    return render(request, 'accounts/login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists. Please login.")
            return redirect('login')

        # Create the user
        User.objects.create_user(username=username, password=password)
        messages.success(request, "User created successfully. Please login.")
        return redirect('login')

    return render(request, 'accounts/signup.html')


def shopping_view(request):
    # This view requires login. So check:
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'accounts/shopping.html')
