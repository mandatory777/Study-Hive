# Generated by Django 5.1.2 on 2025-01-06 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_studygroup_members_studygroup_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='study_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]