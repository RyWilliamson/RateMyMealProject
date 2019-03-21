from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
import os
import json

# This class is the base class for representing user data.
class Chef(AbstractUser):
    username = models.CharField(max_length=128, null= True, unique=True)
    email = models.CharField(max_length=128, null= True)
    password = models.CharField(max_length=128, null= True)
    slug = models.SlugField(blank = True, unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(Chef, self).save(*args, **kwargs)

    USERNAME_FIELD = 'username'

# This class links user data to their profile.
class UserProfile(models.Model):
    user = models.OneToOneField(Chef)
    created = models.DateTimeField(default = timezone.now)
    picture = models.ImageField(upload_to='profile_image', blank=False)
   
    def __str__(self):
        return self.user.username

# This is the class for representing a professional chef, it inherits from Chef.
class Professional(Chef):
    class Meta:
        permissions = ( 
            ( "read_chef", "Can read Chef" ),
        )

# This is the class for representing a homecook chef, it inherits from Chef.
class Casual(Chef):
    class Meta:
        permissions = ( 
            
        )

# This is the class for representing a category.
class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(blank = True, unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# This is a helper function for setting the filepath for recipe images.
def _get_upload_path(self, filename):
    return os.path.join("recipe_images/" + self._get_category_slug() + "/" + filename )

# This is the class for representing a recipe.
class Recipe(models.Model):
    category = models.ForeignKey(Category)
    chef = models.ForeignKey(UserProfile, null = True)
    recipe_name = models.TextField()
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    recipe_ingredients = models.TextField()
    recipe_directions = models.TextField()
    image = models.ImageField(upload_to = _get_upload_path)
    slug = models.SlugField(blank = True, unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipe_name

    # This function returns a list, which is decoded from the JSON stored in the database.
    def get_ingredients(self):
        return json.decoder.JSONDecoder().decode(self.recipe_ingredients)

    # This function is used to convert a list into JSON format for storage.
    def set_ingredients(self, ingredients):
        self.recipe_ingredients = json.dumps(ingredients)

    def _get_category_slug():
        return self.category.slug


class RecipeProfile(models.Model):
    image = models.ImageField(upload_to='profile_images', blank=True)
    recipe = models.OneToOneField(Recipe)
    

    def __str__(self):
        return self.recipe.recipe_name


class Like(models.Model):
    chef = models.ForeignKey(Chef)
    recipe = models.ForeignKey(Recipe)
    created = models.DateTimeField(auto_now_add=True)

    def new(user_id, recipe_id):
        new_like, created = Like.objects.get_or_create(chef=Chef.objects.filter(id=user_id)[0],
                                                       recipe_id=recipe_id)
        return not created
