from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

class admin(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username