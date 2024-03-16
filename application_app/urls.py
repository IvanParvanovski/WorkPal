from django.urls import path

from application_app.permissions import make_application_moderator
from application_app.views import JobOfferApplicationCreateView, ProjectApplicationCreateView, AcceptApplication, \
    RejectApplication, ApplicationJobOfferDetails, ApplicationProjectDetails

main_urls = [
    # Actions
    path('accept/<int:application_id>', AcceptApplication.as_view(), name='accept_application'),
    path('reject/<int:application_id>', RejectApplication.as_view(), name='reject_application'),

    # Details views
    path('details/job_offer/<int:application_id>',
         ApplicationJobOfferDetails.as_view(), name='job_offer_application_details'),
    path('details/project/<int:application_id>',
         ApplicationProjectDetails.as_view(), name='project_application_details'),

    # Create views
    path('add/job_offer/<int:job_offer_id>', JobOfferApplicationCreateView.as_view(),
         name='create_job_offer_application'),
    path('add/project/<int:project_id>', ProjectApplicationCreateView.as_view(),
         name='create_project_application'),
]

permissions_urls = [
    # Permissions of the app
    path('make_application_moderator/<int:user_to_grant_rights_id>', make_application_moderator, name='make_application_moderator'),
]


