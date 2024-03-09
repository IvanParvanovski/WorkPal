from django.views.generic import DetailView

from listing_app.models.job_offer import JobOffer


class JobOfferDetailView(DetailView):
    model = JobOffer
    template_name = 'listing_app/job_offer_detail.html'
