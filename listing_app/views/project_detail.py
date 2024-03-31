from django.views.generic import DetailView

from listing_app.models.project import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'listing_app/project_detail.html'
    pk_url_kwarg = 'project_id'

    def get_object(self, queryset=None):
        # Customize the logic to fetch the object using 'project_id' field
        return self.get_queryset().get(id=self.kwargs['project_id'])
