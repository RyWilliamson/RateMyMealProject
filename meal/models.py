from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser, User

class Chef(AbstractUser):
    username = models.CharField(max_length=128, null= True, unique=True)
    email = models.CharField(max_length=128, null= True)
    password = models.CharField(max_length=128, null= True)

    USERNAME_FIELD = 'username'
    


class UserProfile(models.Model):
    user = models.OneToOneField(Chef)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
   
    def __str__(self):
        return self.user.username
    
class Professional(Chef):
    class Meta:
        permissions = ( 
            ( 'read_chef', 'Can read Chef' ),
        )

class Casual(Chef):
    class Meta:
        permissions = ( 
            
        )
