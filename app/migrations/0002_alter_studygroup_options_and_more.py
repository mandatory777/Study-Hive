# Generated by Django 5.1.2 on 2025-01-03 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studygroup',
            options={'permissions': [('can_edit_own_group', 'Can edit own study group'), ('can_delete_own_group', 'Can delete own study group')]},
        ),
        migrations.RenameField(
            model_name='studygroup',
            old_name='user',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='studygroup',
            name='created_at',
        ),
    ]
