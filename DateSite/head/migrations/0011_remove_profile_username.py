# Generated by Django 4.2.2 on 2023-10-15 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0010_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
