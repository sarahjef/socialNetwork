from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # password = forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput)
    #


    # class Meta:
    #
    #     model = User
    #     fields = ('username', 'first_name', 'email')
    # #
    # # def clean_email(self):
    # #     cd = self.cleaned_data
    # #     if cd['username'] != cd['email']:
    # #         raise forms.ValidationError('Username is invalid,it should be exactly your email')
    # #     return cd['username']
    #
    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']