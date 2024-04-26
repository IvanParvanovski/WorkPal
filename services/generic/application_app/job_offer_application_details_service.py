from application_app.models.job_offer_application_details import JobOfferApplicationDetails
from services.interfaces.application_app.job_offer_application_details_interface import JobOfferApplicationDetailsInterface


class JobOfferApplicationDetailsService(JobOfferApplicationDetailsInterface):
    @staticmethod
    def create_job_offer_details(cv, motivation_letter: str, commit=True) -> JobOfferApplicationDetails:
        job_offer_details = JobOfferApplicationDetails(cv=cv, motivation_letter=motivation_letter)

        if commit:
            job_offer_details.save()

        return job_offer_details

    @staticmethod
    def get_all_job_offer_details():
        return JobOfferApplicationDetails.objects.all()

    @staticmethod
    def get_job_offer_details_by_id(_id: int) -> JobOfferApplicationDetails:
        return JobOfferApplicationDetails.objects.get(id=_id)

    @staticmethod
    def delete_job_offer_details(job_offer_details: JobOfferApplicationDetails):
        job_offer_details.delete()

    @staticmethod
    def delete_job_offer_by_id(_id: int):
        job_offer_details = JobOfferApplicationDetailsService.get_job_offer_details_by_id(_id=_id)
        job_offer_details.delete()

    @staticmethod
    def edit_job_offer_by_id(_id: int, motivation_letter, commit=True) -> JobOfferApplicationDetails:
        job_offer_details = JobOfferApplicationDetailsService.get_job_offer_details_by_id(_id=_id)
        job_offer_details.motivation_letter = motivation_letter

        if commit:
            job_offer_details.save()

        return job_offer_details
