from abc import ABC, abstractmethod

from application_app.models.job_offer_application_details import JobOfferApplicationDetails


class JobOfferApplicationDetailsInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_job_offer_details(cv, motivation_letter: str, commit=True) -> JobOfferApplicationDetails:
        pass

    @staticmethod
    @abstractmethod
    def get_all_job_offer_details():
        pass

    @staticmethod
    @abstractmethod
    def get_job_offer_details_by_id(_id: int) -> JobOfferApplicationDetails:
        pass

    @staticmethod
    @abstractmethod
    def delete_job_offer_details(job_offer_details: JobOfferApplicationDetails):
        pass

    @staticmethod
    @abstractmethod
    def delete_job_offer_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_job_offer_by_id(_id: int, motivation_letter, commit=True) -> JobOfferApplicationDetails:
        pass