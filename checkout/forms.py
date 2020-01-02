from django import forms  
from . import models

class CheckoutForm(forms.ModelForm):
    # country = forms.CharField(
    #     max_length=30,
    #     widget=forms.Select(choices = countries, attrs={'class': "form-control"}),
    # )
    # payment_option = forms.ChoiceField(
    #     choices = payment_options,
    #     widget=forms.RadioSelect(attrs={'class': "payment-options"})
    # )
    # terms_agreed = forms.BooleanField(required=True)
    first_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your FirstName"
            }))
    last_name = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your LastName"
            }))
    # company_name = forms.CharField(max_length=30, 
    #     widget=forms.TextInput(attrs=
    #         {
    #             'class': "form-control", 
    #             "placeholder": "Company Name"
    #         }))
    first_address = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your First Address"
            }))
    second_address = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Your Second Address"
            }))

    town = forms.CharField(max_length=30, 
        widget=forms.TextInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Town or City"
            }))

    # state = forms.CharField(max_length=30, 
    #     widget=forms.TextInput(attrs=
    #         {
    #             'class': "form-control", 
    #             "placeholder": "State Province"
    #         }))
    # zip_code = forms.IntegerField(
    #     widget=forms.NumberInput(attrs=
    #         {
    #             'class': "form-control", 
    #             "placeholder": "Zip / Postal"
    #         }))
    email_address = forms.EmailField(
        widget=forms.EmailInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Email Address"
            }))

    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs=
            {
                'class': "form-control", 
                "placeholder": "Phone Number"
            }))

    class Meta:  
        model = models.Checkout
        fields = ("first_name","last_name","first_address", "second_address","town","email_address","phone_number")