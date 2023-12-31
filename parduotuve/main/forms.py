from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(label='Vartotojo vardas', widget=forms.TextInput(attrs={'autofocus ':'True',
    'class':'form-control'}))
    password = forms.CharField(label='Slaptažodis', widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Vartotojo vardas", widget=forms.TextInput(attrs={'autofocus ':'True',
    'class':'form-control'}))
    email = forms.EmailField(label='Elektroninis pastas', widget=forms.EmailInput(attrs={
    'class':'form-control'}))
    password1 = forms.CharField(label='Slaptažodis', widget=forms.PasswordInput(attrs={
    'class':'form-control'}))
    password2 = forms.CharField(label='Pakartokite Slaptažodi', widget=forms.PasswordInput(attrs={
    'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Senas slaptažodis", widget=forms.PasswordInput(attrs={'autofocus ':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label="Naujas slaptažodis", widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label="Pakartoti slaptažodi", widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="Naujas slaptažodis", widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label="Pakartoti slaptažodi", widget=forms.PasswordInput(attrs=
    {'autocomplete':'current-password','class': 'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=['vardas','pavarde','salis','miestas','telefonas','zipcode']
        widgets={
            'vardas':forms.TextInput(attrs={'class':'form-control'}),
            'pavarde':forms.TextInput(attrs={'class': 'form-control'}),
            'salis':forms.Select(attrs={'class': 'form-control'}),
            'miestas':forms.TextInput(attrs={'class': 'form-control'}),
            'telefonas':forms.NumberInput(attrs={'class': 'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class': 'form-control'}),
        }