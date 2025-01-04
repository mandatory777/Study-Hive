from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login  # Renamed to auth_login for clarity
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages  # Import the messages framework
from .models import StudyGroup
from .forms import StudyGroupForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # Custom error messages
    error_messages = {
        'username': {
            'unique': "This username is already taken. Please choose a different one.",
        },
        'password_mismatch': "The two password fields didn't match. Please check and try again.",
    }



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            auth_login(request, user)  
            messages.success(request, 'Your account has been created successfully! You are now logged in.')
            return redirect('dashboard')  
        else:
            messages.error(request, 'There was an issue with your registration. Please check the form below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            request.session['username'] = ''
            request.session['password'] = ''
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            request.session['username'] = username
            request.session['password'] = password
            return render(request, 'login.html')

    
    request.session['username'] = ''
    request.session['password'] = ''
    return render(request, 'login.html')


def logout_view(request):
    logout(request)  
    return redirect('login')  

def dashboard(request):
    study_groups = [
        {"name": "Mathmatics Group", "description": "Join others in learning complex equations."},
        {"name": "History Group", "description": "Discuss historical events and timelines"},
        {"name": "Coding Group", "description": "Work with others on crafting clean brilliant code."},
        {"name": "Trading Group", "description": "Understand the ins and outs of the matrix with others by learning how to trade the market."},

    ]
    return render(request, 'dashboard.html', {'study_groups': study_groups})

@login_required
def study_groups_list(request):
    study_groups = StudyGroup.objects.all()
    return render(request, 'study_groups_list.html', {'study_groups': study_groups})



def create_study_group(request):
    if request.method == 'POST':
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            study_group = form.save(commit=False)  
            study_group.user = request.user  
            study_group.save()  
            return redirect('dashboard')  
    else:
        form = StudyGroupForm()  
    return render(request, 'study_group_form.html', {'form': form})

@login_required
@permission_required('app_name.can_edit_own_group', raise_exception=True)
def study_group_update(request, pk):
    study_group = get_object_or_404(StudyGroup, pk=pk, user=request.user)  
    if request.method == 'POST':
        form = StudyGroupForm(request.POST, instance=study_group)  
        if form.is_valid():
            form.save()  
            return redirect('study_group_list')  
    else:
        form = StudyGroupForm(instance=study_group)  
    return render(request, 'study_group_form.html', {'form': form})

@login_required
@permission_required('app_name.can_delete_own_group', raise_exception=True)
def study_group_delete(request, pk):
    study_group = get_object_or_404(StudyGroup, pk=pk, user=request.user)  
    if request.method == 'POST':
        study_group.delete()  
        return redirect('study_group_list')  
    return render(request, 'study_group_confirm_delete.html', {'study_group': study_group})
