from django.forms import ModelForm

from listing_app.models.listing import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'location', 'images', 'description']
