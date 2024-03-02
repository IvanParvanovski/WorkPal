from abc import ABC, abstractmethod

from accounts_app.models import CustomUser
from accounts_app.models.profile import Profile


class ProfileInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_profile(user: CustomUser,
                       job_title: str,
                       description: str,
                       image_path: str,
                       commit=True):
        pass

    @staticmethod
    @abstractmethod
    def get_all_profiles():
        pass

    @staticmethod
    @abstractmethod
    def get_profile_by_id(_id: int) -> Profile:
        pass

    @staticmethod
    @abstractmethod
    def delete_profile(profile: Profile):
        pass

    @staticmethod
    @abstractmethod
    def delete_profile_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_profile_by_id(_id: int,
                           job_title: str,
                           description: str,
                           image_path: str,
                           commit=True):
        pass
