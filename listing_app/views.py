from django import forms
from django.shortcuts import render

from company_profiles_app.models.company_identifiers import CompanyIdentifiers
from listing_app.models.job_offer import JobOffer
from listing_app.models.project import Project

from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe

from listing_app.models.listing_identifiers import ListingIdentifiers
from listing_app.widgets import CustomGridSliderWidget, widgets
# from listing_app.models.user_suggestion import UserSuggestion

from listing_app.models.project import *


class CustomForm(forms.Form):
    custom_field = forms.CharField(widget=widgets['custom_widget'])
    # other_pop_up_field = forms.ChoiceField(widget=forms.Select(), choices=JobOffer.WorkCommitment)
    # other_field = forms.ChoiceField(widget=widgets['custom_select'], choices=JobOffer.WorkCommitment)


def test_slider(request):
    # form = CustomForm()

    # if request.POST:
    #     identifiers = ListingIdentifiers.objects.create(type='email', value='example@example.com')
    #     # user_suggestion = UserSuggestion.objects.create(field_name='example_field', suggestion='example_suggestion')
    #
    #     # Create instances of Listing and save them
    #     listing1 = Listing.objects.create(
    #         title='IBM Intern',
    #         location='Sofia airport centre',
    #         identifiers=identifiers,
    #         images='https://images.unsplash.com/photo-1581332512741-35c1cbaef477?q=80&w=3735&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    #         description='Develop applications with WatsonAPI',
    #         content_type=ContentType.objects.get_for_model(JobOfferProxy),  # Set content type for JobOfferProxy
    #         object_id=0  # Set object id to 0, it will be updated later after creation of JobOfferProxy
    #     )
    #
    #     listing2 = Listing.objects.create(
    #         title='Develop Stripe',
    #         location='Tintqva 124',
    #         identifiers=identifiers,  # Link with the created ListingIdentifiers instance
    #         images='https://images.unsplash.com/photo-1553729459-efe14ef6055d?q=80&w=3540&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
    #         description='Facilitate financial services',
    #         content_type=ContentType.objects.get_for_model(ProjectProxy),  # Set content type for ProjectProxy
    #         object_id=0  # Set object id to 0, it will be updated later after creation of ProjectProxy
    #     )
    #
    #     # Create instances of the proxy models and associate them with the Listings
    #     job_offer_proxy = JobOfferProxy.objects.create(
    #         listing=listing1,
    #         benefits='Flexible schedule and free water bottles',
    #         salary_range_min=1000,
    #         salary_range_max=5000,
    #         work_environment='hybrid',
    #         work_commitment='full_time',
    #         key_responsibilities='Be responsible for the WATSON API',
    #         required_qualifications='basic knowledge of programming',
    #         preferred_qualifications='know some Networking',
    #         remote_option=True,
    #         # user_suggestions=user_suggestion  # Link with the created UserSuggestion instance
    #     )
    #
    #     project_proxy = ProjectProxy.objects.create(
    #         listing=listing2,
    #         wage=2000,
    #         preferred_payment='Cash',
    #         status='in_progress',
    #         estimated_duration='5 days'
    #     )
    #
    #     # Update the object_id for the Listing instances with the IDs of the associated proxy models
    #     listing1.object_id = job_offer_proxy.pk
    #     listing2.object_id = project_proxy.pk
    #     listing1.save()
    #     listing2.save()

    # context = {
    #     'title': 'We are in!',
    #     'job_offers': JobOffer.objects.all(),
    #     'projects': Project.objects.all(),
    # }



    return render(request, 'sliderform.html', context={})
