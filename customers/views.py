from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import customer


# --------------------------
# ACCOUNT PAGE (Login/Register or Profile)
# --------------------------
def show_account(request):
    # If user is logged in, show account info
    if request.user.is_authenticated:
        try:
            profile = customer.objects.get(user=request.user)
        except customer.DoesNotExist:
            profile = None
        return render(request, 'account.html', {'profile': profile})

    # Handle POST request (Login/Register)
    if request.method == 'POST':
        # --------------------------
        # REGISTER
        # --------------------------
        if 'register' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')

            # Check if username/email exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('account')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return redirect('account')

            # Create user
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            # Create customer profile
            profile = customer.objects.create(user=user, name=username, phone=phone, address=address)
            profile.save()

            messages.success(request, "Account created successfully! You can now login.")
            return redirect('account')

        # --------------------------
        # LOGIN
        # --------------------------
        elif 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
        
                return redirect('account')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('account')

    # GET request → show forms
    return render(request, 'account.html')


# --------------------------
# LOGOUT
# --------------------------
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('account')


# --------------------------
# HOME PAGE (after login)
# --------------------------
def home(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to login first.")
        return redirect('account')

    # Optional: get customer info
    try:
        profile = customer.objects.get(user=request.user)
    except customer.DoesNotExist:
        profile = None

    return render(request, 'index.html', {'user': request.user, 'profile': profile})
