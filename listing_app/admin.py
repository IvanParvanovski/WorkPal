from django.contrib import admin

from listing_app.models.job_offer import JobOffer
from listing_app.models.listing_identifiers import ListingIdentifiers
from listing_app.models.project import Project

admin.site.register(JobOffer)
admin.site.register(ListingIdentifiers)
admin.site.register(Project)


# Register your models here.
