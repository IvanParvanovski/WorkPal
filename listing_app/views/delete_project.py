from django.shortcuts import redirect
from django.views import View

from services.generic.listing_app.listing_service import ListingService
from services.generic.listing_app.project_service import ProjectService


class DeleteProjectView(View):
    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        project = ProjectService.get_project_by_id(project_id)

        ListingService.delete_listing_by_id(_id=project.listing.id)
        ProjectService.delete_project_by_id(project_id)
        return redirect('user_projects')
