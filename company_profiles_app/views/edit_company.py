from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from company_profiles_app.forms.company_form import CompanyForm
from company_profiles_app.forms.company_identifiers_form import CompanyIdentifiersForm
from services.generic.company_profiles_app.company_identifiers_service import CompanyIdentifiersService
from services.generic.company_profiles_app.company_service import CompanyService
from shared_app.utils import has_company_permission


class EditCompanyView(LoginRequiredMixin, View):
    form_class_company = CompanyForm
    form_class_company_identifiers = CompanyIdentifiersForm
    template_name = 'company_profiles_app/edit_company.html'

    # @method_decorator(permission_required('company_profiles_app.change_company', raise_exception=True))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        company_id = kwargs.get('company_id')
        company = CompanyService.get_company_by_id(company_id)

        if not has_company_permission(request.user, 'company_profiles_app', 'can_change_company',
                                      company.name):
            raise PermissionDenied

        phone_identifier = CompanyIdentifiersService.get_company_identifier_phone_number(company_id).value
        email_identifier = CompanyIdentifiersService.get_company_identifier_email(company_id).value

        context = {
            'company_form': self.form_class_company(instance=company),
            'company_identifiers': self.form_class_company_identifiers(initial={'email': email_identifier,
                                                                                'phone_number': phone_identifier})
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        company_form = self.form_class_company(request.POST, request.FILES)
        company_identifiers_form = self.form_class_company_identifiers(request.POST)

        if company_form.is_valid() and company_identifiers_form.is_valid():
            company_id = kwargs.get('company_id')
            company = CompanyService.get_company_by_id(company_id)

            if not has_company_permission(request.user, 'company_profiles_app', 'can_change_company',
                                          company.name):
                raise PermissionDenied

            phone_identifier = CompanyIdentifiersService.get_company_identifier_phone_number(company_id)
            email_identifier = CompanyIdentifiersService.get_company_identifier_email(company_id)

            CompanyService.edit_company(_id=company_id,
                                        address=company_form.cleaned_data['address'],
                                        secondary_address=company_form.cleaned_data['secondary_address'],
                                        name=company_form.cleaned_data['name'],
                                        company_logo=company_form.cleaned_data['company_logo'],
                                        website=company_form.cleaned_data['website'])

            CompanyIdentifiersService.edit_identifier_by_id(_id=phone_identifier.id,
                                                            _type='phone_number',
                                                            value=company_identifiers_form.cleaned_data['phone_number'],
                                                            company=company)

            CompanyIdentifiersService.edit_identifier_by_id(_id=email_identifier.id,
                                                            _type='email',
                                                            value=company_identifiers_form.cleaned_data['email'],
                                                            company=company)

            return redirect('user_companies')

        context = {
            'company_form': company_form,
            'company_identifiers': company_identifiers_form,
        }

        return render(request, self.template_name, context=context)
