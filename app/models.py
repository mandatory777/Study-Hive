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
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        permissions = [
            ("can_edit_own_group", "Can edit own study group"),
            ("can_delete_own_group", "Can delete own study group"),
        ]


    def __str__(self):
        return self.name
    
