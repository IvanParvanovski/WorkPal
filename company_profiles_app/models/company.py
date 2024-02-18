import os
from pathlib import Path

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from WorkPal import settings


class Company(models.Model):
    class Meta:
        permissions = [
            ('verify_company', 'Can verify the company if it is legit'),
        ]

    @staticmethod
    def get_file_extension(file_path):
        """
        Get the extension of a file and return it

        :param file_path: random_company_logo.jpg
        :return: .jpg
        """
        return Path(file_path).suffix

    def get_absolute_path_to_company_storage(self):
        return settings.MEDIA_ROOT + f'/images/companies/company_{self.id}'

    def get_relative_path_to_company_storage(self):
        return f'images/companies/company_{self.id}'

    def save_company_logo(instance, filename):
        extension = Company.get_file_extension(filename)

        result = f'{instance.get_relative_path_to_company_storage()}' \
                 f'/company_logo{extension}'

        return result

    address = models.CharField(max_length=192)
    secondary_address = models.CharField(max_length=192)
    company_logo = models.ImageField(upload_to=save_company_logo, default='images/default/default_company_img.jpg')
    name = models.CharField(max_length=160)
    website = models.URLField(max_length=128)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    @property
    def days_since_creation(self):
        """
        Calculate the number of days since the company registration.
        """

        delta = timezone.now() - self.registered_at
        return delta.days


@receiver(pre_save, sender=Company)
def delete_old_profile_pic_when_save(sender, *args, **kwargs):
    """
    Deletes the existing company logo to avoid name conflicts with new uploads.
    """

    instance = kwargs['instance']
    path = Company.get_absolute_path_to_company_storage(instance)

    if os.path.exists(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print(files)

        for f in files:
            if 'company_logo' in f:
                os.remove(path + '/' + f)
                break
