from django.urls import path, include

from company_profiles_app.views.create_company import CreateCompanyView
from company_profiles_app.views.delete_company import DeleteCompanyView
from company_profiles_app.views.edit_company import EditCompanyView
from company_profiles_app.views.employment_create_view import EmploymentCreateView
from company_profiles_app.views.handle_association_requests import AcceptAssociationRequest, RejectAssociationRequest
from company_profiles_app.views.permissions.make_rights_manager import make_rights_manager
from company_profiles_app.views.permissions.make_association_moderator import make_associate_moderator
from company_profiles_app.views.response_create_new_company import ResponseCreateNewCompany
from company_profiles_app.views.response_send_association_request import ResponseSendAssociationRequest
from company_profiles_app.views.search_company import search_company


dashboard_urls = [
    path('add/', CreateCompanyView.as_view(), name='create_company'),
    path('add/ci=<int:company_id>', EmploymentCreateView.as_view(), name='create_association'),
    path('edit/<int:company_id>', EditCompanyView.as_view(), name='edit_company'),
    path('delete/<int:company_id>', DeleteCompanyView.as_view(), name='delete_company'),
]

responses_urls = [
    path('success_add_new_company/', ResponseCreateNewCompany.as_view(), name='success_create_new_company'),
    path('success_send_association_request/', ResponseSendAssociationRequest.as_view(),
         name='success_send_association_request'),
]


main_urls = [
    path('responses/', include(responses_urls)),

    # Actions
    path('accept_association/<int:employment_request_id>', AcceptAssociationRequest.as_view(),
         name='accept_association_request'),
    path('reject_association/<int:employment_request_id>', RejectAssociationRequest.as_view(),
         name='reject_association_request'),
    path('search/', search_company, name='search_company'),
]

permissions_urls = [
    path('make_association_moderator/<int:user_to_grant_rights_id>/<int:company_id>', make_associate_moderator,
         name='make_association_moderator'),
    path('make_rights_manager/<int:user_to_grant_rights_id>/<int:company_id>', make_rights_manager,
         name='make_rights_manager'),
]

