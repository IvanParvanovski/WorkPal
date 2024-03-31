from django.shortcuts import render

from company_profiles_app.models import Company
from services.generic.company_profiles_app.company_service import CompanyService


def search_company(request):
    search_text = request.POST.get('search')
    found_companies = CompanyService.get_verified_companies(search_text)

    context = {'found_companies': found_companies}
    return render(request, 'company_profiles_app/search_company_results.html', context=context)
