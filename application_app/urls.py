from django.urls import path

from application_app.views import JobOfferApplicationCreateView, ProjectApplicationCreateView, AcceptApplication, \
    RejectApplication, ApplicationJobOfferDetails, ApplicationProjectDetails

urlpatterns = [
    # dashboard
    path('accept_application/<int:application_id>', AcceptApplication.as_view(), name='accept_application'),
    path('reject_application/<int:application_id>', RejectApplication.as_view(), name='reject_application'),
    path('details_application/job_offer/<int:application_id>',
         ApplicationJobOfferDetails.as_view(), name='job_offer_application_details'),
    path('deatils_application/project/<int:application_id>',
         ApplicationProjectDetails.as_view(), name='project_application_details'),

    path('create_job_offer_application/<int:pk>', JobOfferApplicationCreateView.as_view(),
         name='create_job_offer_application'),
    path('create_project_application/<int:pk>', ProjectApplicationCreateView.as_view(),
         name='create_project_application'),
]
