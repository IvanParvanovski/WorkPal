from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

from services.generic.company_profiles_app.employment_service import EmploymentService


class AcceptAssociationRequest(View):
    def post(self, request, *args, **kwargs):
        association_request = EmploymentService.get_employment_by_id(kwargs.get('employment_id'))
        EmploymentService.set_employment_is_associate_to_true(association_request)
        EmploymentService.set_employment_is_checked_to_true(association_request)

        return redirect('dashboard')


class RejectAssociationRequest(View):
    def post(self, request, *args, **kwargs):
        association_request = EmploymentService.get_employment_by_id(kwargs.get('employment_id'))
        EmploymentService.set_employment_is_checked_to_true(association_request)

        return redirect('dashboard')

# def accept_association_request(request, *args, **kwargs):
#     print('hi')
#     if request.POST:
#         print(request)
#         print(kwargs.get('company_id'))
#     return HttpResponse('in')
