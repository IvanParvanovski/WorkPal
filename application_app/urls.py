from django.urls import path

from application_app.views import JobOfferApplicationDetailsView, ProjectApplicationDetailsView

urlpatterns = [
    path('create_job_offer_application/<int:pk>', JobOfferApplicationDetailsView.as_view(), name='create_job_offer_application'),
    path('create_project_application/<int:pk>', ProjectApplicationDetailsView.as_view(), name='create_project_application'),
]
