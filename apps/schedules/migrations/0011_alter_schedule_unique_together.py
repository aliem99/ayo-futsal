# Generated by Django 5.1.7 on 2025-04-08 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0010_alter_hour_options_alter_schedule_hour'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together={('date', 'hour')},
        ),
    ]
