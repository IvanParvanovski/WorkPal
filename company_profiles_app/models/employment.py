import os

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

from company_profiles_app.models.company import Company
from accounts_app.models.profile import Profile
from shared_app.models import UserSuggestion


class Employment(models.Model):
    class Meta:
        permissions = [
            ('verify_associate', 'Can verify if a person is associated with the given company'),
            ('give_rights', 'Can delegate permissions to other associates to manage company resources and data.'),
        ]

    class CompanyRoles(models.TextChoices):
        OWNER = 'owner', _('Owner')
        HUMAN_RESOURCES = 'human_resources', _('Human Resources')
        RECRUITER = 'recruiter', _('Recruiter')
        HIRING_MANAGER = 'hiring_manager', _('Hiring Manager')
        EMPLOYEE = 'employee', _('Employee')
        INTERN = 'intern', _('Intern')
        OTHER = 'other', _('Other')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=15, choices=CompanyRoles, blank=False, null=False)
    is_associate = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    suggestions = GenericRelation(UserSuggestion)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'Employment(job_t={self.job_title}, pi={self.profile_id}, ci={self.company_id}, is_a={self.is_associate})'


