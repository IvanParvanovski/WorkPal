from django import forms


class JobOfferApplicationDetailsForm(forms.Form):
    cv = forms.FileField()
    motivation_letter = forms.CharField(widget=forms.Textarea)

