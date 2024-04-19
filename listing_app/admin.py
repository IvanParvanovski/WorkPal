from django.contrib import admin

from listing_app.models.industry import Industry
from listing_app.models.job_offer import JobOffer
from listing_app.models.listing import Listing
from listing_app.models.listing_identifiers import ListingIdentifiers
from listing_app.models.project import Project

admin.site.register(JobOffer)
admin.site.register(ListingIdentifiers)
admin.site.register(Project)
admin.site.register(Industry)
admin.site.register(Listing)
