from django.forms import ModelForm
from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class Userform(UserCreationForm):
    helper = FormHelper()
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),


        }