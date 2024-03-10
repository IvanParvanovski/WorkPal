from abc import ABC, abstractmethod

from company_profiles_app.models import Company


class CompanyInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_company(address: str,
                       secondary_address: str,
                       company_logo,
                       name: str,
                       website: str,
                       commit=True):
        pass

    @staticmethod
    @abstractmethod
    def get_company_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def get_companies_by_profile_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_company_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_company(company: Company):
        pass

    @staticmethod
    @abstractmethod
    def edit_company(_id: int,
                     address: str,
                     secondary_address: str,
                     company_logo,
                     name: str,
                     website: str,
                     commit=True):
        pass
