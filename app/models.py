from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User)  

    def __str__(self):
        return self.name  
    
class Event(models.Model):
    group = models.ForeignKey(Group, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title    
    
    class Meta:
        permissions = [
            ("can_edit_own_group", "Can edit own study group"),
            ("can_delete_own_group", "Can delete own study group"),
        ]


    def __str__(self):
        return self.name
    
class Announcement(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="announcements")
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Activity(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="activities")
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Activity in {self.group.name} by {self.user.username} at {self.timestamp}"
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False) 

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} - {self.subject}"