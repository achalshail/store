
from django import forms  
#from . import models
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    password = forms.CharField(min_length= 5, widget=forms.PasswordInput)

    class Meta:  
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email':'Email'
        }