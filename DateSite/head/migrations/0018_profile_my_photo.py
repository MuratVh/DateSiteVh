# Generated by Django 4.1.7 on 2023-10-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0017_myphotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='my_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
