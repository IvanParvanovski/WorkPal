from django.urls import path

from listing_app.views.create_job_offer import CreateJobOfferView
from listing_app.views.create_project import CreateProjectView
from listing_app.views.delete_job_offer import DeleteJobOfferView
from listing_app.views.delete_project import DeleteProjectView
from listing_app.views.edit_job_offer import EditJobOfferView
from listing_app.views.edit_project import EditProjectView
from listing_app.views.job_offer_detail import JobOfferDetailView
from listing_app.views.job_offers_catalog import JobOffersCatalog
from listing_app.views.listing_catalog import ListingCatalog, search_listings
from listing_app.views.permissions.make_listings_manager import make_listings_manager
from listing_app.views.project_detail import ProjectDetailView
from listing_app.views.projects_catalog import ProjectsCatalog

# from listing_app.views import test_slider

dashboard_projects_urls = [
    path('add/', CreateProjectView.as_view(), name='create_project'),
    path('edit/<int:project_id>', EditProjectView.as_view(), name='edit_project'),
    path('delete/<int:project_id>', DeleteProjectView.as_view(), name='delete_project'),
]

dashboard_job_offers_urls = [
    path('add/', CreateJobOfferView.as_view(), name='create_job_offer'),
    path('edit/<int:job_offer_id>', EditJobOfferView.as_view(), name='edit_job_offer'),
    path('delete/<int:job_offer_id>', DeleteJobOfferView.as_view(), name='delete_job_offer'),
]

main_urls = [
    path('projects/', ProjectsCatalog.as_view(), name='projects_catalog'),
    path('projects/<int:project_id>', ProjectDetailView.as_view(), name='project_detail'),

    path('job_offers/', JobOffersCatalog.as_view(), name='job_offers_catalog'),
    path('job_offers/<int:job_offer_id>', JobOfferDetailView.as_view(), name='job_offer_detail'),

    path('listings/<str:industry>', ListingCatalog.as_view(), name='listings_catalog'),
    path('listings/search/', search_listings, name='listings_catalog_search'),
]

permissions_urls = [
    path('make_listings_manager/<int:user_to_grant_rights_id>/<int:company_id>', make_listings_manager, name='make_listings_manager'),
]

