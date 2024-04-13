# Generated by Django 4.2.2 on 2023-10-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0006_profile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('мужчина', 'мужчина'), ('женщина', 'женщина'), ('трансформер', 'трансформер')], max_length=255)),
                ('age_min', models.IntegerField(null=True)),
                ('age_max', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=255)),
                ('education', models.CharField(choices=[('Полное среднее', 'Полное среднее'), ('Среднее специальное', 'Среднее специальное'), ('Высшее', 'Высшее')], max_length=255)),
                ('status', models.CharField(choices=[('В активном поиске', 'В активном поиске'), ('Влюблен(а)', 'Влюблен(а)'), ('Встречается', 'Встречается'), ('В гражданском браке', 'В гражданском браке'), ('Помолвлен(а)', 'Помолвлен(а)'), ('Женат(Замужем)', 'Женат(Замужем)'), ('Все сложно', 'Все сложно'), ('Не женат(Не замужем)', 'Не женат(Не замужем)')], max_length=255)),
            ],
        ),
    ]
