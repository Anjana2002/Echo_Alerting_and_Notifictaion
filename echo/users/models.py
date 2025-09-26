from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    
    email = models.EmailField(unique=True)   
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username

