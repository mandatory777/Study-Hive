# Generated by Django 5.1.2 on 2025-01-10 19:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_studygroup_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='study_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]