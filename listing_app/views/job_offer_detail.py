from django.views.generic import DetailView

from listing_app.models.job_offer import JobOffer
from services.generic.company_profiles_app.employment_service import EmploymentService


class JobOfferDetailView(DetailView):
    model = JobOffer
    template_name = 'listing_app/job_offer_detail.html'
    pk_url_kwarg = 'job_offer_id'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_associate'] = EmploymentService.get_associates_for_company(company_id=)

    def get_object(self, queryset=None):
        # Fetch the object using 'company_id' instead of the default 'pk'
        return self.get_queryset().get(id=self.kwargs['job_offer_id'])
