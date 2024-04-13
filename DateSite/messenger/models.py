from django.db import models
from django.contrib.auth.models import User
from head.models import *



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=True)
    companion = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='my_companions')
    date = models.DateTimeField(auto_now_add=True, null=True)
    
