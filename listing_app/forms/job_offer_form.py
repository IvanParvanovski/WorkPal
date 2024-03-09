from django import forms
from django.forms import ModelForm

from listing_app.models.job_offer import JobOffer
from shared_app.widgets import widgets


class JobOfferForm(ModelForm):
    class Meta:
        model = JobOffer
        fields = [
            'benefits', 'key_responsibilities', 'required_qualifications', 'preferred_qualifications', 'remote_option'
        ]

    salary_range = forms.CharField(widget=widgets['custom_widget'])
    work_environment = forms.ChoiceField(widget=widgets['custom_select'], choices=JobOffer.WorkEnvironment)
    work_commitment = forms.ChoiceField(widget=widgets['custom_select'], choices=JobOffer.WorkCommitment)

