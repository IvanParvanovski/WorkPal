from django.urls import path

from company_profiles_app.views import CreateCompanyView, search_company, EmploymentCreateView

urlpatterns = [
    path('create_company/', CreateCompanyView.as_view(), name='create_company'),
    path('create_employment/ci=<int:company_id>', EmploymentCreateView.as_view(), name='create_employment'),
    path('search_company/', search_company, name='search_company'),
]
