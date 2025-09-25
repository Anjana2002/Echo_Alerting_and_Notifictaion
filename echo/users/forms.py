from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Team

class SignupForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False, empty_label='Select a organinzation')
    class Meta:
        model = User
        fields = ('username', 'team', 'email', 'phone_number', 'password1', 'password2')
    