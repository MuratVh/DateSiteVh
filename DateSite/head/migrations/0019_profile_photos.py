# Generated by Django 4.1.7 on 2023-10-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0018_profile_my_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
