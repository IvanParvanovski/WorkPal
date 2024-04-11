from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from services.generic.company_profiles_app.company_service import CompanyService
from shared_app.utils import has_company_permission


class DeleteCompanyView(LoginRequiredMixin, View):

    # @method_decorator(permission_required('company_profiles_app.delete_company', raise_exception=True))
    def post(self, request, *args, **kwargs):
        company_id = kwargs.get('company_id')
        company = CompanyService.get_company_by_id(company_id)

        if not has_company_permission(request.user, 'company_profiles_app', 'can_delete_company',
                                      company.name):
            raise PermissionDenied

        CompanyService.delete_company_by_id(company_id)
        return redirect('user_companies')
