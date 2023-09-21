from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    Username= models.OneToOneField(User, on_delete= models.CASCADE)
    Address= models.TextField()
    Pic= models.ImageField()