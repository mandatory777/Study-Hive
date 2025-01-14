from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, StudyGroupForm
from .models import StudyGroup, Profile
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
#from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .forms import ProfileForm
from .forms import BioForm, UserForm, SignupForm
from .forms import SignupForm




def home(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print("here")
        if form.is_valid():
            print(form)
            user = form.save()
     # Only create the profile if it dont exist already
            if not Profile.objects.filter(user=user).exists():
                
                Profile.objects.create(user=user)

            return redirect('login') 
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def create_study_group(request):
    if request.user.username != 'adavis':
        return HttpResponseForbidden("You are not allowed to create a group.")
    if request.method == "POST":
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            study_group = form.save(commit=False)
            study_group.created_by = request.user
            study_group.save()
            return redirect('study_group_list')
    else:
        form = StudyGroupForm()
    return render(request, 'create_study_group.html', {'form': form})



@login_required
def study_group_detail(request, pk):
    study_group = get_object_or_404(StudyGroup, pk=pk)

    if request.method == "POST":
        if request.user not in study_group.members.all():
            study_group.members.add(request.user)
            messages.success(request, f"You have joined the group {study_group.name}.")
        else:
            messages.info(request, f"You are already a member of {study_group.name}.")
        return redirect('study_group_detail', pk=pk)

    return render(request, 'study_group_detail.html', {'study_group': study_group})





@login_required
def join_study_group(request, pk):
    study_group = get_object_or_404(StudyGroup, pk=pk)
    
  
    if request.user not in study_group.members.all():
        study_group.members.add(request.user)
        profile = Profile.objects.get(user=request.user)
        profile.study_groups.add(study_group) 
        messages.success(request, f"You have joined the group {study_group.name}.")
    else:
        messages.info(request, f"You are already a member of {study_group.name}.")

    return redirect('study_group_list')

@login_required
def joined_groups(request):
    profile = Profile.objects.get(user=request.user)
    joined_groups = profile.study_groups.all()  # Getting allthe study groups the user has joined
    return render(request, 'joined_groups.html', {'joined_groups': joined_groups})

@login_required
def update_study_group(request, pk):
    study_group = get_object_or_404(StudyGroup, pk=pk)
    if study_group.created_by != request.user and request.user.username != 'adavis':
        return redirect('study_group_list')

    if request.method == 'POST':
        form = StudyGroupForm(request.POST, instance=study_group)
        if form.is_valid():
            form.save()
            return redirect('study_group_list')
    else:
        form = StudyGroupForm(instance=study_group)
    return render(request, 'update_study_group.html', {'form': form})

@login_required
def delete_study_group(request, pk):
    if request.user.username != 'adavis':
        return HttpResponseForbidden("You are not allowed to delete this group.")
    group = get_object_or_404(StudyGroup, pk=pk)
    group.delete()
    return redirect('study_group_list')

@login_required
def study_group_list(request):
    study_groups = StudyGroup.objects.all()  
    return render(request, 'study_group_list.html', {'study_groups': study_groups})


@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    study_groups = profile.study_groups.all()  
    return render(request, 'profile.html', {'profile': profile, 'study_groups': study_groups})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        profile_form = BioForm(request.POST, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()  
            user_form.save() 
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        profile_form = BioForm(instance=profile)
        user_form = UserForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'profile_form': profile_form, 'user_form': user_form})


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        bio = request.POST.get('bio')  #bio from the form
        if bio != profile.bio:
            profile.bio = bio
            profile.save()
            return redirect('profile') 
   
    study_groups = profile.user.joined_groups.all()  
    return render(request, 'profile.html', {'profile': profile, 'study_groups': study_groups})




@login_required
def edit_bio(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = BioForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your bio has been updated!")
            return redirect('profile')
    else:
        form = BioForm(instance=profile)
    return render(request, 'edit_bio.html', {'form': form})



@login_required
def dashboard(request):
    study_groups = StudyGroup.objects.all() 
    return render(request, 'dashboard.html', {'study_groups': study_groups})

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: #only creating if it dont exist
        if not Profile.objects.filter(user=instance).exists():
            Profile.objects.create(user=instance)