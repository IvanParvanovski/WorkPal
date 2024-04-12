from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.listing_app.job_offer_service import JobOfferService


def do_job_offers_exist(companies_job_offers):
    if len(companies_job_offers) == 0:
        return False

    for c in companies_job_offers:
        if len(c) == 0:
            return False
    return True


class UserJobOffersView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/user_job_offers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.request.user.profile
        user_companies = CompanyService.get_user_companies(profile_id=profile.id)
        companies_job_offers = JobOfferService.get_job_offers_for_companies(user_companies)
        context['companies_job_offers'] = companies_job_offers
        context['do_job_offers_exist'] = do_job_offers_exist(companies_job_offers)

        return context

