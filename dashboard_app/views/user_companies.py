from django.views.generic import TemplateView

from services.generic.company_profiles_app.company_service import CompanyService


class UserCompaniesView(TemplateView):
    template_name = 'dashboard/user_companies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_companies'] = CompanyService.get_companies_by_profile_id(_id=self.request.user.profile.id)
        return context
