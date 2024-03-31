import shutil

from cloudinary.models import CloudinaryField

from WorkPal import settings
from pathlib import Path
from django.db import models
from accounts_app.models import CustomUser
from company_profiles_app.models import Company
from listing_app.models.listing import Listing


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    image = CloudinaryField('image')
    companies = models.ManyToManyField(Company, through='company_profiles_app.Employment')
    applications = models.ManyToManyField(Listing, through='application_app.Application')

    def __repr__(self):
        return self.user.username

    def __str__(self):
        return self.__repr__()
