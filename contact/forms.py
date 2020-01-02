from django import forms 
from . import models 

class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={'class': "form-control"}),
    )

    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    message = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    class Meta:  
        model = models.Contact
        fields = ("first_name", "last_name", "email", "subject", "message")
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }