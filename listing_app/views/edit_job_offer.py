from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from listing_app.forms.job_offer_form import JobOfferForm
from listing_app.forms.listing_form import ListingForm
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService


class EditJobOfferView(LoginRequiredMixin, View):
    form_class_listing = ListingForm
    form_class_job_offer = JobOfferForm
    template_name = 'listing_app/edit_job_offer.html'

    @method_decorator(permission_required('listing_app.change_joboffer'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        job_offer_id = kwargs.get('job_offer_id')
        job_offer = JobOfferService.get_job_offer_by_id(_id=job_offer_id)
        listing = job_offer.listing
        selected_options = ListingService.get_all_listing_industries(listing)
        print(selected_options)
        context = {
            'listing_form': self.form_class_listing(instance=listing, initial={'industries': selected_options}),
            'job_offer_form': self.form_class_job_offer(instance=job_offer, profile=request.user.profile),
        }

        return render(request, EditJobOfferView.template_name, context)

    def post(self, request, *args, **kwargs):
        combined_data = request.POST.copy()
        combined_data['salary_range'] = request.POST['thumb1Position'] + ' ' + request.POST['thumb2Position']
        listing_form = self.form_class_listing(request.POST, request.FILES)

        profile = request.user.profile
        job_offer_form = self.form_class_job_offer(profile, combined_data)

        if job_offer_form.is_valid() and listing_form.is_valid():
            job_offer_id = kwargs.get('job_offer_id')
            job_offer = JobOfferService.get_job_offer_by_id(_id=job_offer_id)
            listing = job_offer.listing

            listing = ListingService.edit_listing_by_id(_id=listing.id,
                                                        title=listing_form.cleaned_data['title'],
                                                        location=listing_form.cleaned_data['location'],
                                                        description=listing_form.cleaned_data['description'])

            salary_range_min, salary_range_max = [round(float(x), 2) for x in job_offer_form.cleaned_data['salary_range'].split(' ')]

            if salary_range_min <= 100 and salary_range_max <= 100:
                salary_min_value = round(salary_range_min / 100 * 200000)
                salary_max_value = round(salary_range_max / 100 * 200000)
            else:
                salary_min_value = salary_range_min
                salary_max_value = salary_range_max

            JobOfferService.edit_job_offer_by_id(_id=job_offer_id,
                                                 company=job_offer_form.cleaned_data['company'],
                                                 benefits=job_offer_form.cleaned_data['benefits'],
                                                 salary_range_min=salary_min_value,
                                                 salary_range_max=salary_max_value,
                                                 work_environment=job_offer_form.cleaned_data['work_environment'],
                                                 work_commitment=job_offer_form.cleaned_data['work_commitment'],
                                                 key_responsibilities=job_offer_form.cleaned_data['key_responsibilities'],
                                                 required_qualifications=job_offer_form.cleaned_data['required_qualifications'],
                                                 preferred_qualifications=job_offer_form.cleaned_data['preferred_qualifications'],
                                                 remote_option=job_offer_form.cleaned_data['remote_option'])

            current_industries = ListingService.get_all_listing_industries(listing)
            newly_selected_industries = listing_form.cleaned_data['industries']

            # Add new industries
            for industry in newly_selected_industries:
                if industry not in current_industries:
                    ListingService.add_industry_to_listing(listing, industry)

            # Remove unselected industries
            for industry in current_industries:
                if industry not in newly_selected_industries:
                    ListingService.remove_industry_from_listing(listing, industry)

            return redirect('user_job_offers')

        else:
            print(listing_form.errors)
            print(job_offer_form.errors)

        return HttpResponse('invalid')
