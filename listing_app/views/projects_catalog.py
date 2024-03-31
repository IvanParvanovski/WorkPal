from django.views.generic import TemplateView

from services.generic.listing_app.project_service import ProjectService
from django.core.paginator import Paginator


class ProjectsCatalog(TemplateView):
    template_name = 'listing_app/projects_catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects_list = ProjectService.get_all_projects()

        # Set up pagination

        p = Paginator(projects_list, 7)
        page = self.request.GET.get('page')
        projects = p.get_page(page)

        context['projects'] = projects

        return context
