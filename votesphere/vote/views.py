from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Candidate, Vote,ElectionOfficer

def index(request):
    return render(request, 'index.html')

def home(request):
    candidates = Candidate.objects.all()
    return render(request, 'home.html', {'candidates': candidates})

def manager_register(request):
    if request.method == "POST":
        id_number = request.POST['id_number']
        fullname = request.POST['fullname']
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile_picture = request.FILES.get('profile_picture')

        # Validation
        if User.objects.filter(username=username).exists():
            return render(request, 'manager_register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'manager_register.html', {'error': 'Email already registered'})
        if password != confirm_password:
            return render(request, 'manager_register.html', {'error': 'Passwords do not match'})
        if ElectionOfficer.objects.filter(id_number=id_number).exists():
            return render(request, 'manager_register.html', {'error': 'ID number already registered'})

        # Create User and Election Officer
        user = User.objects.create_user(username=username, email=email, password=password)
        ElectionOfficer.objects.create(
            id_number=id_number, fullname=fullname, username=user,
            phonenumber=phonenumber, email=email, address=address,
            profile_picture=profile_picture
        )

        return redirect('manager_login')  # Redirect to login after registration

    return render(request, 'manager_register.html')


def manager_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('manager_dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'manager_login.html', {'error': 'Invalid credentials'})

    return render(request, 'manager_login.html')


@login_required
def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')

@login_required
def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    
    if Vote.objects.filter(user=request.user).exists():
        return render(request, 'home.html', {'error': 'You have already voted!'})
    
    Vote.objects.create(user=request.user, candidate=candidate)
    return render(request, 'home.html', {'message': 'Vote cast successfully!'})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
