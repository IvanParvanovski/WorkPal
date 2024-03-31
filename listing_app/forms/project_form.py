from django import forms
from django.forms import ModelForm

from listing_app.models.project import Project
from shared_app.widgets import widgets


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['wage', 'preferred_payment', 'status', 'estimated_duration']

    # other_field = forms.ChoiceField(widget=widgets['custom_select'], choices=JobOffer.WorkCommitment)
    # status = forms.ChoiceField(widget=widgets['custom_select'], choices=Project.Status)
