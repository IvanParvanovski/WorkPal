from django.db import models
from django.db.models import CASCADE

from listing_app.models.listing import Listing
from shared.models import IdentifiersAbstract


class ListingIdentifiers(IdentifiersAbstract):
    listing = models.ForeignKey(Listing, on_delete=CASCADE, related_name='identifiers')
