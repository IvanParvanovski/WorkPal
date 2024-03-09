from django.views.generic import DetailView

from listing_app.models.project import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'listing_app/project_detail.html'
