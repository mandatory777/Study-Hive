from django.contrib import admin
from .models import Profile, StudyGroup, Group, Event, Announcement, Activity, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'birthdate']
    search_fields = ['user__username', 'bio']
    list_filter = ['birthdate']

admin.site.register(Profile, ProfileAdmin)


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

admin.site.register(StudyGroup, StudyGroupAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    filter_horizontal = ['members']

   
    def has_add_permission(self, request):
        return request.user.is_superuser  

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser 

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'date']
    search_fields = ['title', 'group__name', 'description']
    list_filter = ['date']

admin.site.register(Event, EventAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'created_at']
    search_fields = ['title', 'message']
    list_filter = ['created_at']

admin.site.register(Announcement, AnnouncementAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['group', 'description', 'timestamp', 'user']
    search_fields = ['group__name', 'user__username', 'description']
    list_filter = ['timestamp']

admin.site.register(Activity, ActivityAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'sender', 'receiver', 'timestamp', 'is_read']
    search_fields = ['subject', 'sender__username', 'receiver__username', 'body']
    list_filter = ['is_read', 'timestamp']

admin.site.register(Message, MessageAdmin)

