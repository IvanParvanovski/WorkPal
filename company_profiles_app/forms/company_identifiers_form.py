import re

from django import forms


class CompanyIdentifiersForm(forms.Form):
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=20, label='Phone Number')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Regular expression pattern for a basic phone number validation
        phone_number_pattern = r'^\+?1?\d{9,15}$'
        if not re.match(phone_number_pattern, phone_number):
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone_number
