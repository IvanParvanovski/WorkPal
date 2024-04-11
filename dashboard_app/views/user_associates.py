from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService


class UserAssociatesView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/user_associates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companies = CompanyService.get_user_companies(profile_id=self.request.user.profile.id)

        context['companies_associates'] = EmploymentService.get_associates_for_companies(companies)
        context['has_associates'] = self.has_associates(context['companies_associates'])
        return context

    def has_associates(self, companies_associates):
        print(companies_associates)
        if len(companies_associates) == 0:
            return False

        for ca in companies_associates:
            if not ca.exists():
                return False

        return True
