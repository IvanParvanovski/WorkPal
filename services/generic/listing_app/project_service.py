from accounts_app.models.profile import Profile
from listing_app.models.listing import Listing
from listing_app.models.project import Project
from services.interfaces.listing_app.project_interface import ProjectInterface


class ProjectService(ProjectInterface):
    @staticmethod
    def create_project(profile: Profile,
                       listing: Listing,
                       wage: int,
                       preferred_payment: str,
                       status: Project.Status,
                       estimated_duration: str,
                       commit=True) -> Project:

        project = Project(profile=profile,
                          listing=listing,
                          wage=wage,
                          preferred_payment=preferred_payment,
                          status=status,
                          estimated_duration=estimated_duration)

        if commit:
            project.save()

        return project

    @staticmethod
    def get_all_projects():
        return Project.objects.all()

    @staticmethod
    def get_project_by_id(_id: int) -> Project:
        return Project.objects.get(id=_id)

    @staticmethod
    def get_projects_by_profile_id(_id: int):
        return Project.objects.filter(profile_id=_id)

    @staticmethod
    def delete_project(project: Project):
        project.delete()

    @staticmethod
    def delete_project_by_id(_id: int):
        project = ProjectService.get_project_by_id(_id=_id)
        project.delete()

    @staticmethod
    def edit_project_by_id(_id: int,
                           wage: int,
                           preferred_payment: str,
                           status: Project.Status,
                           estimated_duration: str,
                           commit=True) -> Project:

        project = ProjectService.get_project_by_id(_id=_id)

        project.wage = wage
        project.preferred_payment = preferred_payment
        project.status = status
        project.estimated_duration = estimated_duration

        if commit:
            project.save()

        return project

