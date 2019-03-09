from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser, User

import json


class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    category = models.ForeignKey(Category)
    recipe_name = models.CharField(max_length = 128)
    views = models.IntegerField(default = 0)
    recipe_ingredients = models.TextField(default = "")
    recipe_directions = models.TextField(default = "")
    image = models.ImageField(upload_to = 'recipe_images/', blank = False)

    def __str__(self):
        return self.recipe_name

    def get_ingredients(self):
        return json.decoder.JSONDecoder().decode(self.recipe_ingredients)

    def _get_category_slug():
        return self.category.slug

class Chef(AbstractUser):
    username = models.CharField(max_length=128, null= True, unique=True)
    email = models.CharField(max_length=128, null= True)
    password = models.CharField(max_length=128, null= True)

    USERNAME_FIELD = 'username'

class UserProfile(models.Model):
    user = models.OneToOneField(Chef)
    picture = models.ImageField(upload_to='profile_images', blank=True)
   
    def __str__(self):
        return self.user.username
    
class Professional(Chef):
    class Meta:
        permissions = ( 
            ( "read_chef", "Can read Chef" ),
        )

class Casual(Chef):
    class Meta:
        permissions = ( 
            
        )
