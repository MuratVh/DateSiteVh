# Generated by Django 4.1.7 on 2023-12-25 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0031_remove_profile_companions'),
        ('messenger', '0005_companion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='companion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companions', to='head.profile'),
        ),
        migrations.DeleteModel(
            name='Companion',
        ),
    ]
