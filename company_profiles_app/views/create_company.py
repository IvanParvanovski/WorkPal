from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        context = {
            'company_form': self.form_class_create_company(),
            'company_identifiers': self.form_class_company_identifiers(),
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        company_form = self.form_class_create_company(request.POST, request.FILES)
        company_identifiers_form = self.form_class_company_identifiers(request.POST)

        if company_form.is_valid() and \
                company_identifiers_form.is_valid():

            if not company_form.cleaned_data['company_logo']:
                company_form.cleaned_data['company_logo'] = 'https://res.cloudinary.com/dpjfbxicd/image/upload/v1711847315/default_company_img_hwuiww.jpg'

            company = CompanyService.create_company(address=company_form.cleaned_data['address'],
                                                    secondary_address=company_form.cleaned_data['secondary_address'],
                                                    company_logo=company_form.cleaned_data['company_logo'],
                                                    name=company_form.cleaned_data['name'],
                                                    website=company_form.cleaned_data['website'])

            CompanyIdentifiersService.create_company_identifier_email(value=company_identifiers_form.cleaned_data['email'],
                                                                      company=company)

            CompanyIdentifiersService.create_company_identifier_phone_number(value=company_identifiers_form.cleaned_data['phone_number'],
                                                                             company=company)

            return redirect('success_create_new_company')
            # return render(self.request, 'home/index.html', {'success_message': 'Registration successful'})

        else:
            print(company_form.errors)
            print(company_identifiers_form.errors)

        context = {
            'company_form': company_form,
            'company_identifiers': company_identifiers_form,
        }

        return render(request, self.template_name, context=context)

