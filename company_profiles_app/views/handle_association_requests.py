from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from services.generic.company_profiles_app.employment_service import EmploymentService


class AcceptAssociationRequest(View):
    @method_decorator(permission_required('company_profiles_app.verify_associate', raise_exception=True))
    def post(self, request, *args, **kwargs):
        association_request = EmploymentService.get_employment_by_id(kwargs.get('employment_id'))
        EmploymentService.set_employment_is_associate_to_true(association_request)
        EmploymentService.set_employment_is_checked_to_true(association_request)

        return redirect('dashboard')


class RejectAssociationRequest(View):
    @method_decorator(permission_required('company_profiles_app.verify_associate', raise_exception=True))
    def post(self, request, *args, **kwargs):
        association_request = EmploymentService.get_employment_by_id(kwargs.get('employment_id'))
        EmploymentService.set_employment_is_checked_to_true(association_request)

        return redirect('dashboard')
