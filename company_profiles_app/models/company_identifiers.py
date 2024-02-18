from django.db import models
from django.db.models import CASCADE

from company_profiles_app.models import Company
from shared.models import IdentifiersAbstract


class CompanyIdentifiers(IdentifiersAbstract):
    """
    The types can be the string 'email' or 'phone', and the value is the actual email or phone
    """

    company = models.ForeignKey(Company, on_delete=CASCADE)
