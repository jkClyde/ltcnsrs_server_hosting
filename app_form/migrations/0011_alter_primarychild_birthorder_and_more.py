# Generated by Django 4.2.3 on 2023-12-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0010_alter_primarychild_lengthofstay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarychild',
            name='birthOrder',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='primarychild',
            name='caregiverAge',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='primarychild',
            name='fatherAge',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='primarychild',
            name='motherContact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
