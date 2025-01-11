"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import LoginView
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
   
    path('profile/', views.profile, name='profile'),
    path('edit_bio/', views.edit_bio, name='edit_bio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('create_study_group/', views.create_study_group, name='create_study_group'),
    path('update_study_group/<int:pk>/', views.update_study_group, name='update_study_group'),
    path('delete_study_group/<int:pk>/', views.delete_study_group, name='delete_study_group'),
    path('study_group_list/', views.study_group_list, name='study_group_list'),
    path('join_study_group/<int:pk>/', views.join_study_group, name='join_study_group'),
    path('joined-groups/', views.joined_groups, name='joined_groups'),
    path('study-groups/', views.study_group_list, name='study_group_list'),
    path('study-groups/<int:pk>/', views.study_group_detail, name='study_group_detail'),
]
