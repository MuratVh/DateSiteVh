# Generated by Django 4.1.7 on 2023-10-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0021_alter_profile_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
