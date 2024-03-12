from django.urls import path

from application_app.views import JobOfferApplicationDetailsView, ProjectApplicationDetailsView, AcceptApplication, \
    RejectApplication

urlpatterns = [
    # dashboard
    path('accept_application/<int:application_id>', AcceptApplication.as_view(), name='accept_application'),
    path('reject_application/<int:application_id>', RejectApplication.as_view(), name='reject_application'),

    path('create_job_offer_application/<int:pk>', JobOfferApplicationDetailsView.as_view(), name='create_job_offer_application'),
    path('create_project_application/<int:pk>', ProjectApplicationDetailsView.as_view(), name='create_project_application'),
]
