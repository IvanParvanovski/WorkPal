from django.views.generic import TemplateView

from services.generic.listing_app.job_offer_service import JobOfferService

from django.core.paginator import Paginator


class JobOffersCatalog(TemplateView):
    template_name = 'listing_app/job_offers_catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        job_offers_list = JobOfferService.get_all_job_offers()
        p = Paginator(job_offers_list, 7)
        page = self.request.GET.get('page')
        job_offers = p.get_page(page)

        context['job_offers'] = job_offers

        return context
