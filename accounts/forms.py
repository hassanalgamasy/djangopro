from django import forms 
from django.contrib.auth.forms import UserCreationForm
from.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'phone', 'account_type', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in ['password1', 'password2']:
            self.fields[field].help_text=None