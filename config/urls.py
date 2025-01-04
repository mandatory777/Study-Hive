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
from django.contrib import admin
from django.urls import path
from app import views  # Ensure views is correctly imported

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Authentication paths
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Study group CRUD paths
    path('study-groups/', views.study_groups_list, name='study_group_list'),  # List all study groups
    path('study-groups/create/', views.create_study_group, name='create_study_group'),  # Create a new study group
    path('study-groups/<int:pk>/update/', views.study_group_update, name='study_group_update'),  # Update a study group
    path('study-groups/<int:pk>/delete/', views.study_group_delete, name='study_group_delete'),  # Delete a study group

    # Admin site
    path('admin/', admin.site.urls),
]