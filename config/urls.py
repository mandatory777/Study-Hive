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
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('study_groups/', views.study_groups_list, name='study_group_list'),
    path('study_groups/create/', views.create_study_group, name='create_study_group'),
    path('study_groups/update/<int:pk>/', views.update_study_group, name='update_study_group'),
    path('study_groups/delete/<int:pk>/', views.delete_study_group, name='delete_study_group'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('join_group/<int:group_id>/', views.join_group, name='join_group'),
]

    

