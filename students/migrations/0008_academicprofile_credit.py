# Generated by Django 4.0.3 on 2022-08-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicprofile',
            name='credit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
