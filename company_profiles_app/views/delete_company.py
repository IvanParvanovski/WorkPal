from django.shortcuts import redirect
from django.views import View

from services.generic.company_profiles_app.company_service import CompanyService


class DeleteCompanyView(View):
    def post(self, request, *args, **kwargs):
        company_id = kwargs.get('company_id')
        CompanyService.delete_company_by_id(company_id)
        return redirect('user_companies')
