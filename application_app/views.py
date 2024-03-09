from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from application_app.forms.job_offer_application_details_form import JobOfferApplicationDetailsForm
from application_app.forms.project_application_details_form import ProjectApplicationDetailsForm
from application_app.models import Application
from application_app.models.job_offer_application_details import JobOfferApplicationDetails
from application_app.models.project_application_details import ProjectApplicationDetails
from services.generic.application_app.application_service import ApplicationService
from services.generic.application_app.job_offer_application_details_service import JobOfferApplicationDetailsService
from services.generic.application_app.project_application_details_service import ProjectApplicationDetailsService
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService
from services.generic.listing_app.project_service import ProjectService


# Can be done as a FormView
class JobOfferApplicationDetailsView(View):
    form_class_job_offer_application_details = JobOfferApplicationDetailsForm
    template_name = 'application_app/create_job_offer_application.html'

    def get(self, request, *args, **kwargs):
        context = {
            'job_offer_form': self.form_class_job_offer_application_details()
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        print(request.POST)
        job_offer_application_form = self.form_class_job_offer_application_details(request.POST, request.FILES)

        if job_offer_application_form.is_valid():
            profile = request.user.profile
            listing = JobOfferService.get_job_offer_by_id(kwargs.get('pk')).listing

            job_offer_application = JobOfferApplicationDetailsService.create_job_offer_details(
                cv=job_offer_application_form.cleaned_data['cv'],
                motivation_letter=job_offer_application_form.cleaned_data['motivation_letter']
            )

            ApplicationService.create_application(profile=profile,
                                                  listing=listing,
                                                  content_type=ContentType.objects.get_for_model(
                                                      JobOfferApplicationDetails),
                                                  object_id=job_offer_application.id)

            return HttpResponse('valid')
        else:
            print(job_offer_application_form.errors)

        return HttpResponse('invalid')


class ProjectApplicationDetailsView(View):
    form_class_project_application = ProjectApplicationDetailsForm
    template_name = 'application_app/create_project_application.html'

    def get(self, request, *args, **kwargs):
        context = {
            'project_application_form': self.form_class_project_application()
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        project_application_form = self.form_class_project_application(request.POST, request.FILES)

        if project_application_form.is_valid():
            profile = request.user.profile
            listing = ProjectService.get_project_by_id(kwargs.get('pk')).listing

            project_application = ProjectApplicationDetailsService.create_project_details(motivation_letter=project_application_form.cleaned_data['motivation_letter'])

            ApplicationService.create_application(profile=profile,
                                                  listing=listing,
                                                  content_type=ContentType.objects.get_for_model(ProjectApplicationDetails),
                                                  object_id=project_application.id)

            return HttpResponse('valid')

        print(project_application_form.errors)
        return HttpResponse('invalid')
