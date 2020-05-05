from django import forms
from .models import User

# normal form


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'required': True
        }
    ))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True,
        }
    ))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'required': True,
        }
    ))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
            'required': True
        }
    ))

# model forms


class RegistrationModel(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'email', 'phone'
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                    'required': True
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'required': True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email Address',
                    'required': True,
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone',
                    'required': True
                }
            )
        }
