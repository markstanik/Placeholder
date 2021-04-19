from django import forms
from . import models
from django.contrib.auth.models import User


class CreateExtendedUser(forms.ModelForm):
    class Meta:
        model = models.ExtendedUser
        fields = ['email', 'firstname', 'lastname', 'major', 'location'] 

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': "form-control"}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
