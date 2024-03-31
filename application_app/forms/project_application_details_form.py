from django import forms


class ProjectApplicationDetailsForm(forms.Form):
    motivation_letter = forms.CharField(widget=forms.Textarea)
