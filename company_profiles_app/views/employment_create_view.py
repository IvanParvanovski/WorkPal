from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from company_profiles_app.forms.employment_form import EmploymentForm
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService


class EmploymentCreateView(LoginRequiredMixin, View):
    form_class_employment = EmploymentForm

    def get(self, request, *args, **kwargs):
        context = {
            'employments': EmploymentService.get_all_employments(), # SHOULD BE DELETED
            'employment_form': self.form_class_employment(),
        }

        return render(request, 'company_profiles_app/employment_info.html', context=context)

    def post(self, request, *args, **kwargs):
        employment_form = self.form_class_employment(request.POST)

        if employment_form.is_valid():
            user = request.user
            user_profile = user.profile
            company_id = kwargs.get('company_id')

            company = CompanyService.get_company_by_id(_id=company_id,)
            EmploymentService.create_employment(profile=user_profile,
                                                company=company,
                                                job_title=employment_form.cleaned_data['job_title'])

        return redirect('dashboard')

