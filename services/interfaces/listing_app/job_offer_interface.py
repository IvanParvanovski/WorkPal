from abc import ABC, abstractmethod

from listing_app.models.job_offer import JobOffer
from listing_app.models.listing import Listing


class JobOfferInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_job_offer(listing: Listing,
                         benefits: str,
                         salary_range_min: int,
                         salary_range_max: int,
                         work_environment: JobOffer.WorkEnvironment,
                         work_commitment: JobOffer.WorkCommitment,
                         key_responsibilities: str,
                         required_qualifications: str,
                         preferred_qualifications: str,
                         remote_option: bool) -> JobOffer:
        pass

    @staticmethod
    @abstractmethod
    def get_all_job_offers():
        pass

    @staticmethod
    @abstractmethod
    def get_job_offer_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_job_offer(job_offer: JobOffer):
        pass

    @staticmethod
    @abstractmethod
    def delete_job_offer_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_job_offer_by_id(_id: int,
                             listing: Listing,
                             benefits: str,
                             salary_range_min: int,
                             salary_range_max: int,
                             work_environment: JobOffer.WorkEnvironment,
                             work_commitment: JobOffer.WorkCommitment,
                             key_responsibilities: str,
                             required_qualifications: str,
                             preferred_qualifications: str,
                             remote_option: bool
                             ) -> JobOffer:
        pass
