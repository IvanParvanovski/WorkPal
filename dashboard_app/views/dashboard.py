from django.shortcuts import render

from services.generic.application_app.application_service import ApplicationService
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.project_service import ProjectService


def render_dashboard(request):

    profile_id = request.user.profile.id

    context = {
        # 'companies': EmploymentService.get_associated_companies_by_profile_id(profile_id), # THE COMPANIES YOU ARE ASSOCIATED WITH

        'association_requests': EmploymentService.get_association_requests_by_company_id(5), # THE ASSOCIATION REQUESTS PEOPLE HAVE MADE TO A SPECIFIC COMPANY
        'application_status': ApplicationService.get_applications_by_profile_id(profile_id), # THE APPLICATIONS YOU HAVE MADE TO PROJECTS OR JOB OFFERS
        'applications_to_projects': ApplicationService.get_applications_to_user_project(3)
    }

    print(ApplicationService.get_applications_to_user_project(3))

    return render(request, 'dashboard/dashboard.html', context=context)
