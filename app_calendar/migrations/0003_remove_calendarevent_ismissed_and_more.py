# Generated by Django 4.2.6 on 2023-12-12 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendar', '0002_calendarevent_isfinished_calendarevent_ismissed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevent',
            name='isMissed',
        ),
        migrations.RemoveField(
            model_name='calendarevent',
            name='isUpcoming',
        ),
    ]
