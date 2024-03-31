from django.urls import path, include

from dashboard_app.views.dashboard import render_dashboard
from dashboard_app.views.user_associates import UserAssociatesView
from dashboard_app.views.user_companies import UserCompaniesView
from dashboard_app.views.user_job_offers import UserJobOffersView
from dashboard_app.views.user_projects import UserProjectsView

# from listing_app.urls import dashboard_urls as listing_dashboard_urls
from listing_app.urls import dashboard_projects_urls \
    as listing_dashboard_projects_urls
from listing_app.urls import dashboard_job_offers_urls \
    as listing_dashboard_job_offers_urls
from company_profiles_app.urls import dashboard_urls as company_dashboard_urls


urlpatterns = [
    # Main urls
    path('', render_dashboard, name='dashboard'),
    path('projects/', UserProjectsView.as_view(), name='user_projects'),
    path('job_offers/', UserJobOffersView.as_view(), name='user_job_offers'),
    path('companies/', UserCompaniesView.as_view(), name='user_companies'),
    path('associates/', UserAssociatesView.as_view(), name='user_associates'),

    # Included
    path('projects/', include(listing_dashboard_projects_urls)),
    path('job_offers/', include(listing_dashboard_job_offers_urls)),
    path('companies/', include(company_dashboard_urls)),
    # path('')
]
