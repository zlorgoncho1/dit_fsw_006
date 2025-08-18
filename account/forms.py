from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
                
        if password != password_confirmation:
            self.add_error('password_confirmation', 'Les mots de passe ne correspondent pas')
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Ce nom d\'utilisateur est déjà pris')
        return username
