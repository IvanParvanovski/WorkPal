from abc import ABC, abstractmethod

from company_profiles_app.models import Company
from company_profiles_app.models.company_identifiers import CompanyIdentifiers


class CompanyIdentifiersInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_company_identifier(_type: str, value, company: Company) \
            -> CompanyIdentifiers:
        pass

    @staticmethod
    @abstractmethod
    def get_identifier_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_identifier(identifier: CompanyIdentifiers):
        pass

    @staticmethod
    @abstractmethod
    def delete_identifier_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_identifier_by_id(_id: int, _type: str, value, company: Company) \
            -> CompanyIdentifiers:
        pass
