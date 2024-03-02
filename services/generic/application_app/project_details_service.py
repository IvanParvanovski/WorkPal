from application_app.models.project_details import ProjectDetails
from services.interfaces.application_app.project_details_interface import ProjectDetailsInterface


class ProjectDetailsService(ProjectDetailsInterface):
    @staticmethod
    def create_project_details(motivation_letter: str, commit=True) -> ProjectDetails:
        project_details = ProjectDetails.objects.create(motivation_letter=motivation_letter)

        if commit:
            project_details.save()

        return project_details

    @staticmethod
    def get_all_project_details():
        return ProjectDetails.objects.all()

    @staticmethod
    def get_project_details_by_id(_id: int) -> ProjectDetails:
        return ProjectDetails.objects.get(id=_id)

    @staticmethod
    def delete_project_details(project_details: ProjectDetails):
        project_details.delete()

    @staticmethod
    def delete_project_details_by_id(_id: int):
        project_details = ProjectDetailsService.get_project_details_by_id(_id=_id)
        project_details.delete()

    @staticmethod
    def edit_project_details_by_id(_id: int,
                                   motivation_letter: int,
                                   commit=True) -> ProjectDetails:
        project_details = ProjectDetailsService.get_project_details_by_id(_id=_id)
        project_details.motivation_letter = motivation_letter

        if commit:
            project_details.save()

        return project_details

