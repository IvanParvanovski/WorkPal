from django.contrib import admin

from application_app.models.job_offer_application_details import JobOfferApplicationDetails
from application_app.models.project_application_details import ProjectApplicationDetails
from company_profiles_app.models import Employment

admin.site.register(Employment)
admin.site.register(JobOfferApplicationDetails)
admin.site.register(ProjectApplicationDetails)

# Register your models here.
