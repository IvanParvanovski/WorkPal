from abc import ABC, abstractmethod

from accounts_app.models.profile import Profile
from listing_app.models.listing import Listing
from listing_app.models.project import Project


class ProjectInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_project(profile: Profile,
                       listing: Listing,
                       wage: int,
                       preferred_payment: str,
                       status: Project.Status,
                       estimated_duration: str,
                       commit=True) -> Project:
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
    def get_projects_by_profile_id(_id: int):
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
                           estimated_duration: str,
                           commit=True) -> Project:
        pass
