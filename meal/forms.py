from django import forms
from django.contrib.auth.models import User
from meal.models import Chef, UserProfile, Professional, Casual

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
