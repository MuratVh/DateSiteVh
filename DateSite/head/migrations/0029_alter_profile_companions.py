# Generated by Django 4.1.7 on 2023-12-24 13:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('head', '0028_profile_companions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='companions',
            field=models.ManyToManyField(related_name='companions', to=settings.AUTH_USER_MODEL),
        ),
    ]
