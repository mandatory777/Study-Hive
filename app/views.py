from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SignupForm, StudyGroupForm
from .models import StudyGroup
from django.contrib import messages
def home(request):
    return render(request, 'home.html')




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard') 
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def create_study_group(request):
    if request.user.username != 'adavis': 
        return redirect('study_group_list') 
    
    if request.method == 'POST':
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
    study_group = get_object_or_404(StudyGroup, pk=pk)
    if study_group.created_by != request.user and request.user.username != 'adavis':
        return redirect('study_group_list') 
    
    if request.method == 'POST':
        study_group.delete()
        return redirect('study_group_list') 
    return render(request, 'delete_study_group.html', {'study_group': study_group})



@login_required
def study_group_list(request):
    study_groups = StudyGroup.objects.all() 
    return render(request, 'study_group_list.html', {'study_groups': study_groups})


@login_required
def dashboard(request):
    return redirect('study_group_list') 