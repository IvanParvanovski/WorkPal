from company_profiles_app.models import Company
from listing_app.models.job_offer import JobOffer
from listing_app.models.listing import Listing
from services.interfaces.listing_app.job_offer_interface import JobOfferInterface


class JobOfferService(JobOfferInterface):
    @staticmethod
    def create_job_offer(company: Company,
                         listing: Listing,
                         benefits: str,
                         salary_range_min: int,
                         salary_range_max: int,
                         work_environment: JobOffer.WorkEnvironment,
                         work_commitment: JobOffer.WorkCommitment,
                         key_responsibilities: str,
                         required_qualifications: str,
                         preferred_qualifications: str,
                         remote_option: bool,
                         commit=True) -> JobOffer:

        job_offer = JobOffer(
            company=company,
            listing=listing,
            benefits=benefits,
            salary_range_min=salary_range_min,
            salary_range_max=salary_range_max,
            work_environment=work_environment,
            work_commitment=work_commitment,
            key_responsibilities=key_responsibilities,
            required_qualifications=required_qualifications,
            preferred_qualifications=preferred_qualifications,
            remote_option=remote_option
        )

        if commit:
            job_offer.save()

        return job_offer

    @staticmethod
    def get_all_job_offers():
        return JobOffer.objects.all()

    @staticmethod
    def get_job_offer_by_id(_id: int):
        return JobOffer.objects.get(id=_id)

    @staticmethod
    def get_job_offers_by_company_id(company_id: int):
        return JobOffer.objects.filter(company_id=company_id)

    @staticmethod
    def get_job_offers_for_companies(companies):
        return [JobOfferService.get_job_offers_by_company_id(c.id) for c in companies]

    @staticmethod
    def get_job_offer_by_listing_id(listing_id: int):
        return JobOffer.objects.get(listing_id=listing_id)

    @staticmethod
    def delete_job_offer(job_offer: JobOffer):
        return job_offer.delete()

    @staticmethod
    def delete_job_offer_by_id(_id: int):
        job_offer = JobOfferService.get_job_offer_by_id(_id=_id)
        job_offer.delete()

    @staticmethod
    def edit_job_offer_by_id(_id: int,
                             company: Company,
                             benefits: str,
                             salary_range_min: int,
                             salary_range_max: int,
                             work_environment: JobOffer.WorkEnvironment,
                             work_commitment: JobOffer.WorkCommitment,
                             key_responsibilities: str,
                             required_qualifications: str,
                             preferred_qualifications: str,
                             remote_option: bool,
                             commit=True) -> JobOffer:

        job_offer = JobOfferService.get_job_offer_by_id(_id=_id)

        job_offer.company = company
        job_offer.benefits = benefits
        job_offer.salary_range_min = salary_range_min
        job_offer.salary_range_max = salary_range_max
        job_offer.work_environment = work_environment
        job_offer.work_commitment = work_commitment
        job_offer.key_responsibilities = key_responsibilities
        job_offer.required_qualifications = required_qualifications
        job_offer.preferred_qualifications = preferred_qualifications
        job_offer.remote_option = remote_option

        if commit:
            job_offer.save()

        return job_offer
