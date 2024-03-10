from abc import ABC, abstractmethod

from application_app.models.project_application_details import ProjectApplicationDetails


class ProjectApplicationDetailsInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_project_details(motivation_letter: str, commit=True) -> ProjectApplicationDetails:
        pass

    @staticmethod
    @abstractmethod
    def get_all_project_details():
        pass

    @staticmethod
    @abstractmethod
    def get_project_details_by_id(_id: int) -> ProjectApplicationDetails:
        pass

    @staticmethod
    @abstractmethod
    def delete_project_details(project_details: ProjectApplicationDetails):
        pass

    @staticmethod
    @abstractmethod
    def delete_project_details_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_project_details_by_id(_id: int,
                                   motivation_letter: int,
                                   commit=True) -> ProjectApplicationDetails:
        pass
