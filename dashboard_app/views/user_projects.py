from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from services.generic.listing_app.project_service import ProjectService


class UserProjectsView(LoginRequiredMixin, TemplateView):
    """
    This view renders the projects a person has uploaded in the system and is an owner of
    """

    template_name = 'dashboard/user_projects.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile
        context['user_projects'] = ProjectService.get_projects_by_profile_id(_id=profile.id)
        return context
