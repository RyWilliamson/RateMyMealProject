from django import forms
from django.contrib.auth.models import User
from meal.models import Chef, UserProfile, Professional, Casual, Recipe

class UserFormRegular(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Casual
        fields = ('username','email','password')

class UserFormChef(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Professional
        permissions = ( 
                ( "read_chef", "Can read Chef" ),
            )
        
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class RecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(max_length = 128, help_text = "Please enter the title of the recipe.")
    recipe_ingredients = forms.CharField(max_length=50, help_text = "Please enter the recipe ingredients here")
    recipe_directions = forms.CharField(max_length=200, help_text = "Please enter the recipe steps here")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
        

    class Meta:
        model = Recipe
        exclude = ('category',)
