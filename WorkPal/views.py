from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

from services.generic.listing_app.industry_service import IndustryService


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        industries_icons = {
            'agriculture': 'agriculture',
            'healthcare': 'cardiology',
            'fashion': 'apparel',
            'technology': 'devices',
            'finance': 'attach_money',
            'education': 'school',
            'entertainment': 'stadia_controller',
            'media': 'live_tv',
            'real estate': 'real_estate_agent',
            'energy': 'energy',
            'aerospace': 'rocket_launch',
            'food & beverage': 'restaurant',
            'environmental': 'eco',
            'marketing': 'ad_group',
            'sports': 'exercise',
            'tourism': 'king_bed',
            'interior design': 'chair',
            'retail': 'storefront',
            'construction': 'construction',
            'consulting': 'monitoring',
            'insurance': 'car_crash',
            'biotechnology': 'biotech',
            'e-commerce': 'sell',
            'music': 'headphones',
            'robotics': 'precision_manufacturing',
            'artificial intelligence': 'robot',
            'architecture': 'architecture',
        }

        industries = IndustryService.get_all_industries()

        for i in industries:
            i.icon = industries_icons.get(i.name.lower())

        context['industries'] = industries

        return context


def custom_page_404_not_found(request, exception):
    return render(request, 'responses/error_404.html', status=404)


def custom_page_403_forbidden(request, exception):
    return render(request, 'responses/error_403_forbidden.html', status=403)

