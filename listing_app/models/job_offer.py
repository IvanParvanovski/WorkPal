from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _

from listing_app.models.listing import Listing


class JobOffer(models.Model):
    class WorkEnvironment(models.TextChoices):
        HYBRID = 'hybrid', _('Hybrid')
        REMOTE = 'remote', _('Remote')
        IN_OFFICE = 'in_office', _('In-office')
        OTHER = 'other', _('Other')

    class WorkCommitment(models.TextChoices):
        FULL_TIME = 'full_time', _('Full-Time')
        PART_TIME = 'part_time', _('Part-Time')
        SEASONAL = 'zero_hours', _('Zero-Hours')
        FLEXTIME = 'flextime', _('Flextime')
        OTHER = 'other', _('Other')

    listing = models.OneToOneField(Listing, on_delete=CASCADE, related_name='job_offer')
    benefits = models.TextField(max_length=1500, blank=True)
    salary_range_min = models.PositiveIntegerField(blank=False, default=1000)
    salary_range_max = models.PositiveIntegerField(blank=False, default=5000)
    work_environment = models.CharField(max_length=25, choices=WorkEnvironment, blank=True, null=False)
    work_commitment = models.CharField(max_length=50, choices=WorkCommitment, blank=True, null=False)
    key_responsibilities = models.TextField(max_length=1500, blank=True)
    required_qualifications = models.TextField(max_length=1500, blank=True)
    preferred_qualifications = models.TextField(max_length=1500, blank=True)
    remote_option = models.BooleanField(default=False)
