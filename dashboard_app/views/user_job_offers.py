from django.views.generic import TemplateView

from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.listing_app.job_offer_service import JobOfferService


class UserJobOffersView(TemplateView):
    template_name = 'dashboard/user_job_offers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.request.user.profile
        user_companies = CompanyService.get_companies_by_profile_id(_id=profile.id)
        companies_job_offers = [
            JobOfferService.get_job_offers_by_company_id(company_id=c.id)
            for c in user_companies
        ]
        context['companies_job_offers'] = companies_job_offers

        return context
