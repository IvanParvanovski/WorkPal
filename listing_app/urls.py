from django.urls import path

from listing_app.views.create_job_offer import CreateJobOfferView
from listing_app.views.create_project import CreateProjectView
from listing_app.views.job_offer_detail import JobOfferDetailView
from listing_app.views.job_offers_catalog import JobOffersCatalog
from listing_app.views.project_detail import ProjectDetailView
from listing_app.views.projects_catalog import ProjectsCatalog

# from listing_app.views import test_slider

urlpatterns = [
    # path('', test_slider),
    path('create_project/', CreateProjectView.as_view(), name='create_project'),
    path('create_job_offer/', CreateJobOfferView.as_view(), name='create_job_offer'),

    path('projects_catalog/', ProjectsCatalog.as_view(), name='projects_catalog'),
    path('job_offers_catalog/', JobOffersCatalog.as_view(), name='job_offers_catalog'),


    path('job_offer_details/<int:pk>', JobOfferDetailView.as_view(), name='job_offer_detail'),
    path('project_details/<int:pk>', ProjectDetailView.as_view(), name='project_detail')
]
