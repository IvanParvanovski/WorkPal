from django.urls import path, include

from dashboard_app.views.dashboard import render_dashboard
from dashboard_app.views.user_projects import UserProjectsView
from listing_app.urls import dashboard_urls

urlpatterns = [
    path('', render_dashboard, name='dashboard'),
    path('', include(dashboard_urls)),
    path('projects/', UserProjectsView, name='user_projects'),

]
