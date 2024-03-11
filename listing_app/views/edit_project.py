from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView

from listing_app.forms.listing_form import ListingForm
from listing_app.forms.project_form import ProjectForm
from services.generic.listing_app.listing_service import ListingService
from services.generic.listing_app.project_service import ProjectService


class EditProjectView(View):
    template_name = 'listing_app/edit_project.html'
    form_class_listing = ListingForm
    form_class_project = ProjectForm

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        project = ProjectService.get_project_by_id(project_id)
        listing = ListingService.get_listing_by_id(project.listing.id)

        context = {
            'listing_form': self.form_class_listing(instance=listing),
            'project_form': self.form_class_project(instance=project),
        }

        return render(request, EditProjectView.template_name, context=context)

    def post(self, request, *args, **kwargs):
        project_form = self.form_class_project(request.POST)
        listing_form = self.form_class_listing(request.POST, request.FILES)

        if project_form.is_valid() and listing_form.is_valid():
            project = ProjectService.get_project_by_id(kwargs.get('project_id'))
            listing = ListingService.get_listing_by_id(_id=project.listing.id)

            project_id = kwargs.get('project_id')

            ListingService.edit_listing_by_id(_id=listing.id,
                                              title=listing_form.cleaned_data['title'],
                                              location=listing_form.cleaned_data['location'],
                                              images=listing_form.cleaned_data['images'],
                                              description=listing_form.cleaned_data['description'])

            ProjectService.edit_project_by_id(_id=project_id,
                                              wage=project_form.cleaned_data['wage'],
                                              preferred_payment=project_form.cleaned_data['preferred_payment'],
                                              status=project_form.cleaned_data['status'],
                                              estimated_duration=project_form.cleaned_data['estimated_duration'])
            return redirect('user_projects')
        else:
            print(project_form.errors)
            print(listing_form.errors)

        return HttpResponse('invalid')