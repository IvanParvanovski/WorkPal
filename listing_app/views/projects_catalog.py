from django.views.generic import TemplateView

from services.generic.listing_app.project_service import ProjectService


class ProjectsCatalog(TemplateView):
    template_name = 'listing_app/projects_catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = ProjectService.get_all_projects()
        return context
