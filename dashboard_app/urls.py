from django.urls import path, include

from dashboard_app.views.dashboard import render_dashboard
from dashboard_app.views.user_associates import UserAssociatesView
from dashboard_app.views.user_companies import UserCompaniesView
from dashboard_app.views.user_job_offers import UserJobOffersView
from dashboard_app.views.user_projects import UserProjectsView
from listing_app.urls import dashboard_urls

urlpatterns = [
    path('', render_dashboard, name='dashboard'),
    path('', include(dashboard_urls)),

    path('projects/', UserProjectsView.as_view(), name='user_projects'),
    path('job_offers/', UserJobOffersView.as_view(), name='user_job_offers'),
    path('companies/', UserCompaniesView.as_view(), name='user_companies'),
    path('associates/', UserAssociatesView.as_view(), name='user_associates'),
]
