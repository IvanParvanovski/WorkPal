from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from listing_app.forms.listing_form import ListingForm
from listing_app.forms.project_form import ProjectForm
from services.generic.listing_app.industry_service import IndustryService
from services.generic.listing_app.listing_service import ListingService
from services.generic.listing_app.project_service import ProjectService


class CreateProjectView(LoginRequiredMixin, View):
    form_class_create_listing = ListingForm
    form_class_create_project = ProjectForm
    template_name = 'listing_app/create_project.html'

    def get(self, request, *args, **kwargs):
        listing_form = self.form_class_create_listing()
        project_form = self.form_class_create_project()

        context = {
            'listing_form': listing_form,
            'project_form': project_form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        listing_form = self.form_class_create_listing(request.POST, request.FILES)
        project_form = self.form_class_create_project(request.POST)

        if listing_form.is_valid() and project_form.is_valid():
            listing = ListingService.create_listing(title=listing_form.cleaned_data['title'],
                                                    location=listing_form.cleaned_data['location'],
                                                    description=listing_form.cleaned_data['description'])

            ProjectService.create_project(profile=request.user.profile,
                                          listing=listing,
                                          wage=project_form.cleaned_data['wage'],
                                          preferred_payment=project_form.cleaned_data['preferred_payment'],
                                          status=project_form.cleaned_data['status'],
                                          estimated_duration=project_form.cleaned_data['estimated_duration'])

            for industry in listing_form.cleaned_data['industries']:
                ListingService.add_industry_to_listing(listing, industry)

            return redirect('projects_catalog')
        else:
            print(listing_form.errors)
            print(project_form.errors)

        return HttpResponse('not valid')

