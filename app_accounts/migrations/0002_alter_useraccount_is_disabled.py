# Generated by Django 4.2.3 on 2023-12-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_disabled',
            field=models.BooleanField(default=True),
        ),
    ]
