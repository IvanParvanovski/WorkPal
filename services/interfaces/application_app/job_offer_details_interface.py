from abc import ABC, abstractmethod

from application_app.models.job_offer_details import JobOfferDetails


class JobOfferDetailsInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_job_offer_details(cv, motivation_letter: str) -> JobOfferDetails:
        pass

    @staticmethod
    @abstractmethod
    def get_all_job_offer_details():
        pass

    @staticmethod
    @abstractmethod
    def get_job_offer_details_by_id(_id: int) -> JobOfferDetails:
        pass

    @staticmethod
    @abstractmethod
    def delete_job_offer_details(job_offer_details: JobOfferDetails):
        pass

    @staticmethod
    @abstractmethod
    def delete_job_offer_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_job_offer_by_id(_id: int, motivation_letter) -> JobOfferDetails:
        pass