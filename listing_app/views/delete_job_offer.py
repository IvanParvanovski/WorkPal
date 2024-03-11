from django.shortcuts import redirect
from django.views import View

from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService


class DeleteJobOfferView(View):
    def post(self, request, *args, **kwargs):
        job_offer_id = kwargs.get('job_offer_id')
        job_offer = JobOfferService.get_job_offer_by_id(job_offer_id)

        ListingService.delete_listing(listing=job_offer.listing)
        JobOfferService.delete_job_offer(job_offer)

        return redirect('user_job_offers')
