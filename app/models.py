from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ('can_create_group', 'Can create a study group'),
            ('can_update_group', 'Can update a study group'),
            ('can_delete_group', 'Can delete a study group'),
        ]

    def __str__(self):
        return self.name

