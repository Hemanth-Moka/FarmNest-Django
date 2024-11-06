from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'app/Base.html')


# Home View


# Registration View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'app/register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'app/register.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'app/register.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Optional: Log the user in after registration
        login(request, user)

        messages.success(request, "Registration successful! You can log in now.")
        return redirect('login')

    return render(request, 'app/register.html')


def cart(request):
    return render(request, 'app/cart.html')


def submitpayment(request):
    return render(request, 'app/ordering/submitpayment.html')


from django.shortcuts import render

# View for rendering the buy now page
from django.shortcuts import render


def product_list(request):
    # Logic to fetch products from the database
    return render(request, 'app/products.html')


def product_detail(request, product_id):
    # Logic to fetch the specific product by product_id from the database
    return render(request, 'app/product_detail.html')


# Login View
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('products')  # Redirect to the profile page or any other page
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'app/login.html')


# Logout View
def Logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# Profile View (Login Required)

def profile(request):
    return render(request, 'app/profile.html')


from django.shortcuts import render, redirect
from .models import Payment


def order(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        payment_type = request.POST.get('payment')
        card_number = request.POST.get('signum')
        expiry_date = request.POST.get('expiate')
        cvv = request.POST.get('cvv')

        # Check if all necessary fields are present
        if name and email and address and payment_type and card_number and expiry_date and cvv:
            # Save to the database
            Payment.objects.create(
                name=name,
                email=email,
                address=address,
                payment_type=payment_type,
                card_number=card_number,
                expiry_date=expiry_date,
                cvv=cvv
            )

            return redirect('submitpayment')
        else:
            # Optional: Handle the case where some data is missing
            print("Form data is incomplete.")

    return render(request, 'app/ordering/order.html')


def seeds(request):
    return render(request, 'app/products/seeds.html')


def login_first(request):
    return render(request, 'app/Disclaimer/login_first.html')


def smart_equipments(request):
    return render(request, 'app/products/smart_equipments.html')


def about(request):
    return render(request, 'app/about.html')


'''def about(request):
    return render(request, 'app/ordering/order.html')'''


# Products View
def products(request):
    return render(request, 'app/products.html')


def equipments(request):
    return render(request, 'app/products/equipments.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.shortcuts import render, redirect

def submit_payment(request):
    if request.method == 'POST':
        # Retrieve the payment details
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        payment_type = request.POST.get('payment')
        card_number = request.POST.get('signum')
        exp_date = request.POST.get('expiate')
        cvv = request.POST.get('cvv')

        # Basic validation
        if not all([name, email, address, payment_type, card_number, exp_date, cvv]):
            return redirect('order')  # Redirect back for correction if incomplete

        # Add logic for processing the payment or saving details

        # After processing, render the success template with the user's name
        return render(request, 'app/ordering/submitpayment.html', {'name': name})

    # If not a POST request, redirect to the base page
    return redirect('Base')

