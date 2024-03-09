from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from listing_app.forms.job_offer_form import JobOfferForm
from listing_app.forms.listing_form import ListingForm
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService


class CreateJobOfferView(View):
    form_class_create_listing = ListingForm
    form_class_create_job_offer = JobOfferForm
    template_name = 'listing_app/create_job_offer.html'

    def get(self, request, *args, **kwargs):
        listing_form = self.form_class_create_listing()
        job_offer_form = self.form_class_create_job_offer()
        print(job_offer_form.fields['work_environment'])
        context = {
            'listing_form': listing_form,
            'job_offer_form': job_offer_form
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        combined_data = request.POST.copy()
        combined_data['salary_range'] = request.POST['thumb1Position'] + ' ' + request.POST['thumb2Position']

        listing_form = self.form_class_create_listing(request.POST, request.FILES)
        job_offer_form = self.form_class_create_job_offer(combined_data)

        if job_offer_form.is_valid() and listing_form.is_valid() :

            listing = ListingService.create_listing(title=listing_form.cleaned_data['title'],
                                                    location=listing_form.cleaned_data['location'],
                                                    images=listing_form.cleaned_data['images'],
                                                    description=listing_form.cleaned_data['description'])

            salary_range_min, salary_range_max = [round(float(x), 2) for x in job_offer_form.cleaned_data['salary_range'].split(' ')]

            JobOfferService.create_job_offer(listing=listing,
                                             benefits=job_offer_form.cleaned_data['benefits'],
                                             salary_range_min=salary_range_min,
                                             salary_range_max=salary_range_max,
                                             work_environment=job_offer_form.cleaned_data['work_environment'],
                                             work_commitment=job_offer_form.cleaned_data['work_commitment'],
                                             key_responsibilities=job_offer_form.cleaned_data['key_responsibilities'],
                                             required_qualifications=job_offer_form.cleaned_data['required_qualifications'],
                                             preferred_qualifications=job_offer_form.cleaned_data['preferred_qualifications'],
                                             remote_option=job_offer_form.cleaned_data['remote_option'])

            return redirect('job_offers_catalog')
        else:
            print(listing_form.errors)
            print(job_offer_form.errors)

        return HttpResponse('invalid')
