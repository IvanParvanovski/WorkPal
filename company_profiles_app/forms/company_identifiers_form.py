from django import forms


class CompanyIdentifiersForm(forms.Form):
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=20, label='Phone Number')
