import os
from pathlib import Path

from django.apps import apps

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
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


temp_instance = None


@receiver(pre_save, sender=Company)
def track_changes(sender, instance, **kwargs):
    try:
        original_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return  # New instance, no need to track changes
    instance._previous_state = {field.name: getattr(original_instance, field.name) for field in instance._meta.fields}
    global temp_instance
    temp_instance = instance._previous_state['name']


@receiver(post_save, sender=Company)
def get_instance_after(sender, instance, **kwargs):
    print('After')
    print(instance)


def instance_created(sender, instance, created, **kwargs):
    # Generate a lowercase instance name for use in permission codenames and names
    instance_name = instance.name.lower().replace(" ", "_")

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


def instance_updated(sender, instance, created, **kwargs):
    instance_name_before = temp_instance.lower().replace(" ", "_")
    instance_name_new = instance.name.lower().replace(" ", "_")

    job_offer_model_class = apps.get_model('listing_app', 'JobOffer')
    job_offer_content_type = ContentType.objects.get_for_model(job_offer_model_class)

    company_model_class = apps.get_model('company_profiles_app', 'Company')
    company_content_type = ContentType.objects.get_for_model(company_model_class)

    application_model_class = apps.get_model('application_app', 'Application')
    application_content_type = ContentType.objects.get_for_model(application_model_class)

    employment_model_class = apps.get_model('company_profiles_app', 'Employment')
    employment_content_type = ContentType.objects.get_for_model(employment_model_class)

    perm_can_add_job_offer = Permission.objects.get(codename=f'can_add_job_offer_{instance_name_before}',
                                                    content_type=job_offer_content_type)
    perm_can_change_job_offer = Permission.objects.get(codename=f'can_change_job_offer_{instance_name_before}',
                                                       content_type=job_offer_content_type)
    perm_can_delete_job_offer = Permission.objects.get(codename=f'can_delete_job_offer_{instance_name_before}',
                                                       content_type=job_offer_content_type)
    perm_can_change_company = Permission.objects.get(codename=f'can_change_company_{instance_name_before}',
                                                     content_type=company_content_type)
    perm_can_delete_company = Permission.objects.get(codename=f'can_delete_company_{instance_name_before}',
                                                     content_type=company_content_type)
    perm_can_verify_associate = Permission.objects.get(codename=f'can_verify_associate_{instance_name_before}',
                                                       content_type=company_content_type)
    perm_can_adjudicate_application = Permission.objects.get(codename=f'can_adjudicate_application_{instance_name_before}',
                                                             content_type=application_content_type)
    perm_can_give_rights = Permission.objects.get(codename=f'can_give_rights_{instance_name_before}',
                                                  content_type=employment_content_type)

    perm_can_add_job_offer.codename = f'can_add_job_offer_{instance_name_new}'
    perm_can_change_job_offer.codename = f'can_change_job_offer_{instance_name_new}'
    perm_can_delete_job_offer.codename = f'can_delete_job_offer_{instance_name_new}'
    perm_can_change_company.codename = f'can_change_company_{instance_name_new}'
    perm_can_delete_company.codename = f'can_delete_company_{instance_name_new}'
    perm_can_verify_associate.codename = f'can_verify_associate_{instance_name_new}'
    perm_can_adjudicate_application.codename = f'can_adjudicate_application_{instance_name_new}'
    perm_can_give_rights.codename = f'can_give_rights_{instance_name_new}'

    perm_can_add_job_offer.save()
    perm_can_change_job_offer.save()
    perm_can_delete_job_offer.save()
    perm_can_change_company.save()
    perm_can_delete_company.save()
    perm_can_verify_associate.save()
    perm_can_adjudicate_application.save()
    perm_can_give_rights.save()

    print(instance_name_before)
    print(instance_name_new)


@receiver(post_save, sender=Company)
def create_custom_company_permissions(sender, instance, created, **kwargs):
    if created:
        instance_created(sender, instance, created, **kwargs)
    else:
        instance_updated(sender, instance, created, **kwargs)


@receiver(post_delete, sender=Company)
def delete_company_perms(sender, instance, **kwargs):
    instance_name = instance.name.lower().replace(" ", "_")

    job_offer_model_class = apps.get_model('listing_app', 'JobOffer')
    job_offer_content_type = ContentType.objects.get_for_model(job_offer_model_class)

    company_model_class = apps.get_model('company_profiles_app', 'Company')
    company_content_type = ContentType.objects.get_for_model(company_model_class)

    application_model_class = apps.get_model('application_app', 'Application')
    application_content_type = ContentType.objects.get_for_model(application_model_class)

    employment_model_class = apps.get_model('company_profiles_app', 'Employment')
    employment_content_type = ContentType.objects.get_for_model(employment_model_class)

    perm_can_add_job_offer = Permission.objects.get(codename=f'can_add_job_offer_{instance_name}',
                                                    content_type=job_offer_content_type)
    perm_can_change_job_offer = Permission.objects.get(codename=f'can_change_job_offer_{instance_name}',
                                                       content_type=job_offer_content_type)
    perm_can_delete_job_offer = Permission.objects.get(codename=f'can_delete_job_offer_{instance_name}',
                                                       content_type=job_offer_content_type)
    perm_can_change_company = Permission.objects.get(codename=f'can_change_company_{instance_name}',
                                                     content_type=company_content_type)
    perm_can_delete_company = Permission.objects.get(codename=f'can_delete_company_{instance_name}',
                                                     content_type=company_content_type)
    perm_can_verify_associate = Permission.objects.get(codename=f'can_verify_associate_{instance_name}',
                                                       content_type=company_content_type)
    perm_can_adjudicate_application = Permission.objects.get(codename=f'can_adjudicate_application_{instance_name}',
                                                             content_type=application_content_type)
    perm_can_give_rights = Permission.objects.get(codename=f'can_give_rights_{instance_name}',
                                                  content_type=employment_content_type)

    perm_can_add_job_offer.delete()
    perm_can_change_job_offer.delete()
    perm_can_delete_job_offer.delete()
    perm_can_change_company.delete()
    perm_can_delete_company.delete()
    perm_can_verify_associate.delete()
    perm_can_adjudicate_application.delete()
    perm_can_give_rights.delete()
