from django import forms
from django.utils.translation import gettext as _


class SignInForm(forms.Form):
    email = forms.EmailField(label=_('Email'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
