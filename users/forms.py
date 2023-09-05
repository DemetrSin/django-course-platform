from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Enter Email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email:'})
    )
    username = forms.CharField(
        label='Enter Login:',
        required=True,
        help_text="Cannot be entered symbols: @,_, /",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter login:'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Enter Password:',
        required=True,
        help_text="Password cannot be small and simple",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password:'})
    )
    password2 = forms.CharField(
        label='Confirm Password:',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password:'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter Email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email:'})
    )
    username = forms.CharField(
        label='Enter Login:',
        required=True,
        help_text="Cannot be entered symbols: @,_, /",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter login:'})
    )

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Download photo:',
        required=False,
        widget=forms.FileInput,
    )

    class Meta:
        model = Profile
        fields = ['img']

