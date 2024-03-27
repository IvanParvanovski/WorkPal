from django import forms
from django.forms import ModelForm

from listing_app.models.industry import Industry
from listing_app.models.listing import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'location', 'images', 'description']
        widgets = {
            'images': forms.ClearableFileInput(attrs={'class': 'image-section'})
        }

    industries = forms.ModelMultipleChoiceField(
        queryset=Industry.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to False if industries are not required
    )
