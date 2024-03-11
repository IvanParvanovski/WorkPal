from django import forms
from django.forms import ModelForm

from company_profiles_app.models import Company, Employment
from listing_app.models.job_offer import JobOffer
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService
from shared_app.widgets import widgets


class JobOfferForm(ModelForm):
    def __init__(self, profile, *args, **kwargs):
        super(JobOfferForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = CompanyService.get_user_companies(profile_id=profile.id)
        # self.fields['company'].queryset = Company.objects.filter(employment__profile_id=profile.id)

    class Meta:
        model = JobOffer
        fields = [
            'company', 'benefits', 'key_responsibilities', 'required_qualifications', 'preferred_qualifications', 'remote_option'
        ]

    salary_range = forms.CharField(widget=widgets['custom_widget'])
    work_environment = forms.ChoiceField(widget=widgets['custom_select'], choices=JobOffer.WorkEnvironment)
    work_commitment = forms.ChoiceField(widget=widgets['custom_select'], choices=JobOffer.WorkCommitment)

