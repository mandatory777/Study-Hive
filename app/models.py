from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)


    class Meta:
        permissions = [
            ('can_create_group', 'Can create a study group'),
            ('can_update_group', 'Can update a study group'),
            ('can_delete_group', 'Can delete a study group'),
        ]

    def __str__(self):
        return self.name
    
    #need another model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True, null=True)
    study_groups = models.ManyToManyField(StudyGroup, related_name='profiles')
   
#profile related to a group
#tab for joined groups
#my groups
    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()