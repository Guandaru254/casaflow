from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib import messages




# Create your views here.

def home(request):
    return render(request, 'base.html')  # Ensure 'base.html' exists in your templates folder

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

       # Basic password match validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.first_name = full_name  # Assuming 'first_name' for full name
                user.save()
                
                 # Add the user to the selected group
                group = Group.objects.get(name=role)
                user.groups.add(group)

                # Log in the user and redirect to home
                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Registration failed: {e}")
    return render(request, 'register.html')

def create_groups():
    roles = ['Admin', 'Property Owner', 'Agent', 'Tenant', 'Caretaker']
    for role in roles:
        Group.objects.get_or_create(name=role)

# Run this function as part of a custom management command or include it in a startup script.

