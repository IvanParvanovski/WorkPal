from django.urls import path

from company_profiles_app.views.create_company import CreateCompanyView
from company_profiles_app.views.delete_company import DeleteCompanyView
from company_profiles_app.views.edit_company import EditCompanyView
from company_profiles_app.views.employment_create_view import EmploymentCreateView
from company_profiles_app.views.handle_association_requests import AcceptAssociationRequest, RejectAssociationRequest
from company_profiles_app.views.permissions.make_association_moderator import make_associate_moderator
from company_profiles_app.views.search_company import search_company

urlpatterns = [
    # dashboard
    path('accept_association/<int:employment_id>', AcceptAssociationRequest.as_view(), name='accept_association_request'),
    path('reject_association/<int:employment_id>', RejectAssociationRequest.as_view(), name='reject_association_request'),
    path('permissions/make_associate_moderator/<int:profile_id>', make_associate_moderator, name='make_association_moderator'),

    # main urls
    path('create_company/', CreateCompanyView.as_view(), name='create_company'),
    path('edit_company/<int:company_id>', EditCompanyView.as_view(), name='edit_company'),
    path('delete_company/<int:company_id>', DeleteCompanyView.as_view(), name='delete_company'),
    path('create_employment/ci=<int:company_id>', EmploymentCreateView.as_view(), name='create_employment'),
    path('search_company/', search_company, name='search_company'),
]
