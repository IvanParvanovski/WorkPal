from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from company_profiles_app.forms.company_identifiers_form import CompanyIdentifiersForm
from company_profiles_app.forms.company_form import CompanyForm
from services.generic.company_profiles_app.company_identifiers_service import CompanyIdentifiersService
from services.generic.company_profiles_app.company_service import CompanyService


class CreateCompanyView(LoginRequiredMixin, View):
    form_class_create_company = CompanyForm
    form_class_company_identifiers = CompanyIdentifiersForm

    template_name = 'company_profiles_app/create_company.html'

    def get(self, request, *args, **kwargs):
        # print(f'CREATE COMPANY VIEW - True' if request.htmx else 'CREATE COMPANY VIEW - False')
        context = {
            'company_form': self.form_class_create_company(),
            'company_identifiers': self.form_class_company_identifiers(),
        }
        # print(context)
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        company_form = self.form_class_create_company(request.POST)
        company_identifiers_form = self.form_class_company_identifiers(request.POST)

        # print(company_identifiers_form)
        if company_form.is_valid() and \
                company_identifiers_form.is_valid():

            company = CompanyService.create_company(address=company_form.cleaned_data['address'],
                                                    secondary_address=company_form.cleaned_data['secondary_address'],
                                                    company_logo=company_form.cleaned_data['company_logo'],
                                                    name=company_form.cleaned_data['name'],
                                                    website=company_form.cleaned_data['website'])

            CompanyIdentifiersService.create_company_identifier_email(value=company_identifiers_form.cleaned_data['email'],
                                                                      company=company)

            CompanyIdentifiersService.create_company_identifier_phone_number(value=company_identifiers_form.cleaned_data['phone_number'],
                                                                             company=company)

            return render(self.request, 'home/index.html', {'success_message': 'Registration successful'})

        else:
            print(company_form.errors)
            print(company_identifiers_form.errors)

        return HttpResponse('POST request received')

