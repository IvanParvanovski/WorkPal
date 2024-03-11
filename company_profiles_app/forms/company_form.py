from django.forms import forms, ModelForm

from company_profiles_app.models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'secondary_address', 'website', 'company_logo']




