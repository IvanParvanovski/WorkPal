from django.contrib import admin

from company_profiles_app.models import Company
from company_profiles_app.models.company_identifiers import CompanyIdentifiers


admin.site.register(CompanyIdentifiers)
admin.site.register(Company)

# Register your models here.
