from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from services.generic.application_app.application_service import ApplicationService
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.project_service import ProjectService


@login_required
def render_dashboard(request):

    profile_id = request.user.profile.id
    user_companies = CompanyService.get_user_companies(profile_id=profile_id)

    # Association requests to your companies
    association_requests = EmploymentService.get_association_requests_for_companies(user_companies)

    # Applications made to your projects
    user_projects = ProjectService.get_projects_by_profile_id(profile_id)
    applications_for_projects = ApplicationService.get_applications_for_user_projects(user_projects)

    # Applications you have made to other - statuses
    application_statuses = ApplicationService.get_applications_by_profile_id(profile_id)

    # Job offers
    companies_job_offers = JobOfferService.get_job_offers_for_companies(user_companies)
    applications_for_job_offers = ApplicationService.get_applications_for_companies_job_offers(companies_job_offers)

    context = {
        'association_requests': association_requests,
        'any_association_request': any(inner_list for inner_list in association_requests),

        'application_status': application_statuses,
        'any_applications_statuses': any(inner_list for inner_list in application_statuses),

        'applications_for_projects': applications_for_projects,
        'any_project_applications': any(inner_list for inner_list in applications_for_projects),

        'companies_applications_for_job_offers': applications_for_job_offers,
        'any_job_offers_applications': any(inner_list for inner_list in applications_for_job_offers)
    }

    # print(ApplicationService.get_applications_to_user_project(3))

    return render(request, 'dashboard/dashboard.html', context=context)
