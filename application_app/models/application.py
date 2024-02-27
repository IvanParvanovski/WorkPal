from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts_app.models.profile import Profile
from listing_app.models.listing import Listing
from application_app.models.job_offer_details import JobOfferDetails
from application_app.models.project_details import ProjectDetails


class Application(models.Model):
    is_approved = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ['JobOfferDetails', 'ProjectDetails']})
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
