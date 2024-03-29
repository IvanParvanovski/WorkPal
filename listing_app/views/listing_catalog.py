from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from listing_app.models.listing import Listing
from services.generic.listing_app.industry_service import IndustryService
from services.generic.listing_app.listing_service import ListingService


class ListingCatalog(TemplateView):
    template_name = 'listing_app/listing_catalog.html'

    def get_context_data(self, **kwargs):
        print(kwargs)

        context = super().get_context_data(**kwargs)
        industry_name = kwargs.get('industry').capitalize()
        industry = IndustryService.get_industry_by_name(industry_name)
        context['listings'] = ListingService.get_listings_by_industry(industry)

        return context


def search_listings(request, *args, **kwargs):
    query = request.GET.get('q')
    print(query)

    results = ListingService.search_listings_by_query(query)
    print(results)

    context = {
        'listings': results,
    }

    return render(request, 'listing_app/listing_catalog.html', context=context)


# class ListingCatalogSearch(TemplateView):
#     template_name =
