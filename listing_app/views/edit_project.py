from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView

from listing_app.forms.listing_form import ListingForm
from listing_app.forms.project_form import ProjectForm
from services.generic.listing_app.listing_service import ListingService
from services.generic.listing_app.project_service import ProjectService


class EditProjectView(LoginRequiredMixin, View):
    template_name = 'listing_app/edit_project.html'
    form_class_listing = ListingForm
    form_class_project = ProjectForm

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        project = ProjectService.get_project_by_id(project_id)
        listing = ListingService.get_listing_by_id(project.listing.id)
        selected_options = ListingService.get_all_listing_industries(listing)

        context = {
            'listing_form': self.form_class_listing(instance=listing, initial={'industries': selected_options}),
            'project_form': self.form_class_project(instance=project),
        }

        return render(request, EditProjectView.template_name, context=context)

    def post(self, request, *args, **kwargs):
        project_form = self.form_class_project(request.POST)
        listing_form = self.form_class_listing(request.POST, request.FILES)

        if project_form.is_valid() and listing_form.is_valid():
            project = ProjectService.get_project_by_id(kwargs.get('project_id'))
            listing = ListingService.get_listing_by_id(_id=project.listing.id)

            current_industries = ListingService.get_all_listing_industries(listing)
            newly_selected_industries = listing_form.cleaned_data['industries']
            print(current_industries)
            print(newly_selected_industries)

            # Add new industries
            for industry in newly_selected_industries:
                if industry not in current_industries:
                    ListingService.add_industry_to_listing(listing, industry)

            # Remove unselected industries
            for industry in current_industries:
                if industry not in newly_selected_industries:
                    ListingService.remove_industry_from_listing(listing, industry)

            project_id = kwargs.get('project_id')

            ListingService.edit_listing_by_id(_id=listing.id,
                                              title=listing_form.cleaned_data['title'],
                                              location=listing_form.cleaned_data['location'],
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

        context = {
            'listing_form': listing_form,
            'project_form': project_form,
        }

        return render(request, EditProjectView.template_name, context=context)
