from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICE = [
    ('В активном поиске', 'В активном поиске'),
    ('Влюблен(а)', 'Влюблен(а)'),
    ('Встречается', 'Встречается'),
    ('В гражданском браке', 'В гражданском браке'),
    ('Помолвлен(а)', 'Помолвлен(а)'),
    ('Женат(Замужем)', 'Женат(Замужем)'),
    ('Все сложно', 'Все сложно'),
    ('Не женат(Не замужем)', 'Не женат(Не замужем)')
]
GENDER = [
    ('---', '---'),
    ('мужчина', 'мужчина'),
    ('женщина', 'женщина')
]



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(blank=True, null=True)
    biography = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='default-profile-photo.png', blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER, blank=True)

    def __str__(self):
        return self.user.username
    

class MyPhoto(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='my_photos')
    photo = models.ImageField(blank=True, null=True, upload_to='my_photos/')




