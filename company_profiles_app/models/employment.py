import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

from company_profiles_app.models.company import Company
from accounts_app.models.profile import Profile


class Employment(models.Model):
    class Meta:
        permissions = [
            ('verify_associate', 'Can verify if a person is associated with the given company')
        ]

    class CompanyRoles(models.TextChoices):
        OWNER = 'owner', _('Owner')
        HUMAN_RESOURCES = 'human_resources', _('Human Resources')
        RECRUITER = 'recruiter', _('Recruiter')
        HIRING_MANAGER = 'hiring_manager', _('Hiring Manager')
        EMPLOYEE = 'employee', _('Employee')
        INTERN = 'intern', _('Intern')
        OTHER = 'other', _('Other')

    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=15, choices=CompanyRoles, blank=False, null=False)
    is_associate = models.BooleanField(default=False)


@receiver(pre_save, sender=Profile)
def delete_old_profile_pic_when_save(sender, *args, **kwargs):
    """
    Deletes the existing profile picture to avoid name conflicts with new uploads.
    """

    instance = kwargs['instance']
    path = Profile.get_absolute_path_to_user_profile_storage(instance.user_id)

    if os.path.exists(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print(files)

        for f in files:
            if 'profile_picture' in f:
                os.remove(path + '/' + f)
                break
