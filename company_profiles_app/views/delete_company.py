from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from services.generic.company_profiles_app.company_service import CompanyService


class DeleteCompanyView(LoginRequiredMixin, View):

    @method_decorator(permission_required('company_profiles_app.delete_company', raise_exception=True))
    def post(self, request, *args, **kwargs):
        company_id = kwargs.get('company_id')
        CompanyService.delete_company_by_id(company_id)
        return redirect('user_companies')
