from django import forms
from .models import registration

class formreg(forms.ModelForm):    
    fields = ['first_name', 'last_name', 'username' 'email', 'password1', 'password2']

