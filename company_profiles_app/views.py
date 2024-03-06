from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from company_profiles_app.forms.company_identifiers_form import CompanyIdentifiersForm
from company_profiles_app.forms.create_company_form import CreateCompanyForm
from company_profiles_app.forms.employment_form import EmploymentForm
from company_profiles_app.models import Company, Employment
from services.generic.accounts_app.profile_service import ProfileService
from services.generic.company_profiles_app.company_identifiers_service import CompanyIdentifiersService
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService


class CreateCompanyView(View):
    form_class_create_company = CreateCompanyForm
    form_class_company_identifiers = CompanyIdentifiersForm

    template_name = 'company_profiles_app/create_company.html'

    def get(self, request, *args, **kwargs):
        # print(f'CREATE COMPANY VIEW - True' if request.htmx else 'CREATE COMPANY VIEW - False')
        context = {
            'company_form': self.form_class_create_company(),
            'company_identifiers': self.form_class_company_identifiers(),
            'companies': Company.objects.all(),
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


class EmploymentCreateView(View):
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

        return HttpResponse('POST request received')


# def create_employment(request, company_id):
#     print(request)
#     print(company_id)
#     return HttpResponse('Hello')


def search_company(request):
    search_text = request.POST.get('search')
    found_companies = Company.objects.filter(name__icontains=search_text)

    context = {'found_companies': found_companies}
    return render(request, 'company_profiles_app/search_company_results.html', context=context)
