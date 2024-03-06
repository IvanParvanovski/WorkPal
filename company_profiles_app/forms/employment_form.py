from django.forms import ModelForm

from company_profiles_app.models import Employment


class EmploymentForm(ModelForm):
    class Meta:
        model = Employment
        fields = [
            'job_title'
        ]
