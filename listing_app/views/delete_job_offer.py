from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService
from shared_app.utils import has_company_permission


class DeleteJobOfferView(LoginRequiredMixin, View):
    # @method_decorator(permission_required('listing_app.delete_joboffer', raise_exception=True))
    def post(self, request, *args, **kwargs):
        job_offer_id = kwargs.get('job_offer_id')
        job_offer = JobOfferService.get_job_offer_by_id(job_offer_id)

        if not has_company_permission(request.user,
                                      'listing_app',
                                      'can_delete_job_offer',
                                      job_offer.company.name):
            raise PermissionDenied

        ListingService.delete_listing(listing=job_offer.listing)
        JobOfferService.delete_job_offer(job_offer)

        return redirect('user_job_offers')
