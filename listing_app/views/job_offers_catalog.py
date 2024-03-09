from django.views.generic import TemplateView

from services.generic.listing_app.job_offer_service import JobOfferService


class JobOffersCatalog(TemplateView):
    template_name = 'listing_app/job_offers_catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_offers'] = JobOfferService.get_all_job_offers()
        return context
