from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
    
    
