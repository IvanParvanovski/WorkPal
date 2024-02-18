from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from listing_app.models.listing import Listing
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = 'in_progress', _('In-progress')
        OPEN = 'open', _('Open')
        COMPLETED = 'completed', _('Completed')

    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, related_name='project')
    wage = models.PositiveIntegerField()
    preferred_payment = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=Status)
    estimated_duration = models.CharField(max_length=50)

