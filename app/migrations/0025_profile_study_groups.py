# Generated by Django 5.1.2 on 2025-01-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='study_groups',
            field=models.ManyToManyField(related_name='profiles', to='app.studygroup'),
        ),
    ]
