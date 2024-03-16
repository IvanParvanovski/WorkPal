from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

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
class JobOfferApplicationCreateView(LoginRequiredMixin, View):
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


class ProjectApplicationCreateView(LoginRequiredMixin, View):
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


class ApplicationJobOfferDetails(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'application_app/application_job_offer_details.html'
    context_object_name = 'application'

    def get(self, request, *args, **kwargs):
        # get job offer by application id

        application_id = kwargs.get('application_id')
        application = ApplicationService.get_application_by_id(application_id)
        job_offer_application_details = JobOfferApplicationDetailsService.get_job_offer_details_by_id(_id=application.object_id)

        context = {
            'job_offer_application_details': job_offer_application_details
        }

        return render(request, ApplicationJobOfferDetails.template_name, context=context)


class ApplicationProjectDetails(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'application_app/application_project_details.html'
    context_object_name = 'application'

    def get(self, request, *args, **kwargs):
        application_id = kwargs.get('application_id')
        application = ApplicationService.get_application_by_id(application_id)
        project = ProjectApplicationDetailsService.get_project_details_by_id(_id=application.object_id)

        context = {
            'project': project
        }

        return render(request, ApplicationProjectDetails.template_name, context=context)


class AcceptApplication(LoginRequiredMixin, View):
    @method_decorator(permission_required('application_app.adjudicate_application', raise_exception=True))
    def post(self, request, *args, **kwargs):
        application_id = kwargs.get('application_id')
        application = ApplicationService.get_application_by_id(application_id)
        ApplicationService.set_application_is_approved_true(application)
        ApplicationService.set_application_is_checked_true(application)
        return redirect('dashboard')


class RejectApplication(LoginRequiredMixin, View):
    @method_decorator(permission_required('application_app.adjudicate_application', raise_exception=True))
    def post(self, request, *args, **kwargs):
        application_id = kwargs.get('application_id')
        application = ApplicationService.get_application_by_id(application_id)
        ApplicationService.set_application_is_checked_true(application)
        return redirect('dashboard')
