# Generated by Django 5.1.7 on 2025-04-06 07:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddSchedule',
            new_name='Schedule',
        ),
    ]
