import os
from pathlib import Path

from django.apps import apps

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# from listing_app.models.job_offer import JobOffer


class Company(models.Model):
    # class Meta:
    #     permissions = [
    #         ('verify_company', 'Can verify the company if it is legit'),
    #     ]

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


@receiver(post_save, sender=Company)
def create_custom_company_permissions(sender, instance, created, **kwargs):
    # Check if a new Company instance is being created, not updated
    if created:
        # Generate a lowercase instance name for use in permission codenames and names
        instance_name = instance.name.lower()

        # Get the model classes and content types for the relevant models
        job_offer_model_class = apps.get_model('listing_app', 'JobOffer')
        job_offer_content_type = ContentType.objects.get_for_model(job_offer_model_class)

        company_model_class = apps.get_model('company_profiles_app', 'Company')
        company_content_type = ContentType.objects.get_for_model(company_model_class)

        application_model_class = apps.get_model('application_app', 'Application')
        application_content_type = ContentType.objects.get_for_model(application_model_class)

        employment_model_class = apps.get_model('company_profiles_app', 'Employment')
        employment_content_type = ContentType.objects.get_for_model(employment_model_class)

        # Create custom permissions related to job offers
        Permission.objects.create(
            codename=f'can_add_job_offer_{instance_name}',
            name=f'Can create job offer for {instance_name}',
            content_type=job_offer_content_type,
        )

        Permission.objects.create(
            codename=f'can_change_job_offer_{instance_name}',
            name=f'Can change job offer for {instance_name}',
            content_type=job_offer_content_type,
        )

        Permission.objects.create(
            codename=f'can_delete_job_offer_{instance_name}',
            name=f'Can delete job offer for {instance_name}',
            content_type=job_offer_content_type,
        )

        # Create custom permissions related to companies
        Permission.objects.create(
            codename=f'can_change_company_{instance_name}',
            name=f'Can change company {instance_name}',
            content_type=company_content_type
        )

        Permission.objects.create(
            codename=f'can_delete_company_{instance_name}',
            name=f'Can delete company {instance_name}',
            content_type=company_content_type
        )

        Permission.objects.create(
            codename=f'can_verify_associate_{instance_name}',
            name=f'Can verify associate {instance_name}',
            content_type=company_content_type
        )

        # Create custom permissions related to applications
        Permission.objects.create(
            codename=f'can_adjudicate_application_{instance_name}',
            name=f'Can adjudicate application {instance_name}',
            content_type=application_content_type
        )

        # Create custom permissions related to employments
        Permission.objects.create(
            codename=f'can_give_rights_{instance_name}',
            name=f'Can give rights {instance_name}',
            content_type=employment_content_type
        )
