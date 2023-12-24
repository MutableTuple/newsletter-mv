from django.db import models
from django import forms
from django.forms import ModelForm,TextInput, EmailInput, Textarea, Select, PasswordInput
from .models import Newsletter

class EmailForm(ModelForm):
    class Meta:
        model=Newsletter
        fields=['email']
        widgets = {
            'email': EmailInput(attrs={
                'class': "input form__email", 
                'placeholder': 'Enter your email'
                }),
            } 
  