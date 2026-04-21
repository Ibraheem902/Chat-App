from django.forms import ModelForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'images': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder':'Add Display Name'}),
            'info': forms.Textarea(attrs={'rows':'3','placeholder':'Add Info'}),
        }

class EmailForm(ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['email']