from django.views.generic import TemplateView

from services.generic.listing_app.industry_service import IndustryService


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industries'] = IndustryService.get_all_industries()

        return context
