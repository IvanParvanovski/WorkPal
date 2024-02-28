from abc import ABC, abstractmethod

from listing_app.models.project import Project


class ProjectInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_project(listing,
                       wage: int,
                       preferred_payment: str,
                       status: Project.Status,
                       estimated_duration: str) -> Project:
        pass

    @staticmethod
    @abstractmethod
    def get_all_projects():
        pass

    @staticmethod
    @abstractmethod
    def get_project_by_id(_id: int) -> Project:
        pass

    @staticmethod
    @abstractmethod
    def delete_project(project: Project):
        pass

    @staticmethod
    @abstractmethod
    def delete_project_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_project_by_id(_id: int,
                           wage: int,
                           preferred_payment: str,
                           status: Project.Status,
                           estimated_duration: str) -> Project:
        pass