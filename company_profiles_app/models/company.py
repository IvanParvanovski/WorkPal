import os
from pathlib import Path

from cloudinary.models import CloudinaryField
from django.db import models
from django.utils import timezone


class Company(models.Model):
    class Meta:
        permissions = [
            ('verify_company', 'Can verify the company if it is legit'),
        ]

    address = models.CharField(max_length=192)
    secondary_address = models.CharField(max_length=192)
    company_logo = CloudinaryField('company_logo')
    name = models.CharField(max_length=160)
    website = models.URLField(max_length=128)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    @property
    def days_since_creation(self):
        """
        Calculate the number of days since the company registration.
        """

        delta = timezone.now() - self.registered_at
        return delta.days
