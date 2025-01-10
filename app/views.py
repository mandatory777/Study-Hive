from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import StudyGroup, Group, Message
from .forms import StudyGroupForm, CustomAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from .forms import LoginForm

# Home view
def home(request):
    return render(request, 'home.html')


# Admin check function
def is_admin(user):
    return user.is_staff

# Profile view
def profile_view(request):
    return render(request, 'profile.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Your account has been created successfully! You are now logged in.')
            return redirect('dashboard')  # Redirect to dashboard after successful registration
        else:
            messages.error(request, 'There was an issue with your registration. Please check the form below.')
    else:
        form = UserCreationForm()  # Initialize form for GET request
    return render(request, 'register.html', {'form': form})


# Login view
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    user_groups = Group.objects.filter(members=request.user)
    study_groups = StudyGroup.objects.all()
    received_messages = Message.objects.filter(receiver=request.user)

    context = {
        'received_messages': received_messages,
        'study_groups': study_groups,
        'user_groups': user_groups,
    }

    return render(request, 'dashboard.html', context)


# Join group view
@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if group.members.filter(id=request.user.id).exists():
        return render(request, 'group_already_member.html', {'group': group})
    group.members.add(request.user)
    return redirect('group_detail', group_id=group.id)

# Study groups list view
@login_required
def study_groups_list(request):
    groups = StudyGroup.objects.all()
    return render(request, 'study_group_list.html', {'study_groups': groups})

# (admins)
@login_required
@user_passes_test(is_admin)
def create_study_group(request):
    if request.method == 'POST':
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Study group created successfully!')
            return redirect('study_group_list')
    else:
        form = StudyGroupForm()
    return render(request, 'create_study_group.html', {'form': form})

# Group detail view
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'group_detail.html', {'group': group})

# (admins)
@login_required
@user_passes_test(is_admin)
def update_study_group(request, pk):
    try:
        group = StudyGroup.objects.get(pk=pk)
    except StudyGroup.DoesNotExist:
        messages.error(request, "The group does not exist.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudyGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudyGroupForm(instance=group)

    return render(request, 'update_study_group.html', {'form': form, 'group': group})

# (admins)
@login_required
@user_passes_test(is_admin)
def delete_study_group(request, pk):
    group = get_object_or_404(StudyGroup, pk=pk)
    if request.method == 'POST':
        group.delete()
        messages.success(request, "Group deleted successfully.")
        return redirect('dashboard')
    return render(request, 'delete_study_group.html', {'group': group})
