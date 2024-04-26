from application_app.models.project_application_details import ProjectApplicationDetails
from services.interfaces.application_app.project_application_details_interface import ProjectApplicationDetailsInterface


class ProjectApplicationDetailsService(ProjectApplicationDetailsInterface):
    @staticmethod
    def create_project_details(motivation_letter: str, commit=True) -> ProjectApplicationDetails:
        project_details = ProjectApplicationDetails(motivation_letter=motivation_letter)

        if commit:
            project_details.save()

        return project_details

    @staticmethod
    def get_all_project_details():
        return ProjectApplicationDetails.objects.all()

    @staticmethod
    def get_project_details_by_id(_id: int) -> ProjectApplicationDetails:
        return ProjectApplicationDetails.objects.get(id=_id)

    @staticmethod
    def delete_project_details(project_details: ProjectApplicationDetails):
        project_details.delete()

    @staticmethod
    def delete_project_details_by_id(_id: int):
        project_details = ProjectApplicationDetailsService.get_project_details_by_id(_id=_id)
        project_details.delete()

    @staticmethod
    def edit_project_details_by_id(_id: int,
                                   motivation_letter: str,
                                   commit=True) -> ProjectApplicationDetails:
        project_details = ProjectApplicationDetailsService.get_project_details_by_id(_id=_id)
        project_details.motivation_letter = motivation_letter

        if commit:
            project_details.save()

        return project_details

