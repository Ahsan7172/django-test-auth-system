from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import CustomUser,Bank,LoanRequest

class Signup(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','user_type']
        
class Login(AuthenticationForm):
    class Meta:
        model=CustomUser
        fields=['username','password']
        widgets={'passward':forms.PasswordInput}
class BankForm(forms.ModelForm):
    class Meta:
     model=Bank
     fields=['bank_name','loan_type']
class LoanForm(forms.ModelForm):
    class Meta:
        model=LoanRequest
        fields=['bank','reason','amount','Date','interest_rate','payable_amount']
    
        