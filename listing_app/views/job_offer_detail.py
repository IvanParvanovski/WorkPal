from django.views.generic import DetailView

from listing_app.models.job_offer import JobOffer


class JobOfferDetailView(DetailView):
    model = JobOffer
    template_name = 'listing_app/job_offer_detail.html'
    pk_url_kwarg = 'job_offer_id'

    def get_object(self, queryset=None):
        # Fetch the object using 'company_id' instead of the default 'pk'
        return self.get_queryset().get(id=self.kwargs['job_offer_id'])
