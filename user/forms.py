from django import forms
from django.core.exceptions import ValidationError

from user.models import UserModel


class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)


class ImageUploadForm(forms.Form):
    user_img = forms.ImageField(widget=forms.FileInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput())


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = UserModel
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'placeholder': 'username'
#             }),
#             'password': forms.PasswordInput(attrs={
#                 'placeholder': 'password'
#             })
#         }


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'youremailname@gmail.com'
    }))
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25, required=False)
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Parollar bir xil emas !')
        return self.cleaned_data
