from abc import ABC, abstractmethod

from accounts_app.models.profile import Profile
from company_profiles_app.models import Employment, Company


class EmploymentInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_employment(profile: Profile, company: Company, job_title: str, commit=True) \
            -> Employment:
        pass

    @staticmethod
    @abstractmethod
    def get_all_employments():
        pass

    @staticmethod
    @abstractmethod
    def get_employment_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def get_association_requests_by_company_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_employment(employment):
        pass

    @staticmethod
    @abstractmethod
    def delete_employment_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def set_employment_is_associate_to_true(employment: Employment):
        pass

    @staticmethod
    @abstractmethod
    def edit_employment_by_id(
            _id: int,
            profile: Profile,
            company: Company,
            job_title: str,
            commit=True) -> Employment:
        pass
