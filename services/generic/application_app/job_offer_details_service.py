from application_app.models.job_offer_application_details import JobOfferDetails
from services.interfaces.application_app.job_offer_details_interface import JobOfferDetailsInterface


class JobOfferDetailsService(JobOfferDetailsInterface):
    @staticmethod
    def create_job_offer_details(cv, motivation_letter: str, commit=True) -> JobOfferDetails:
        job_offer_details = JobOfferDetails.objects.create(cv=cv, motivation_letter=motivation_letter)

        if commit:
            job_offer_details.save()

        return job_offer_details

    @staticmethod
    def get_all_job_offer_details():
        return JobOfferDetails.objects.all()

    @staticmethod
    def get_job_offer_details_by_id(_id: int) -> JobOfferDetails:
        return JobOfferDetails.objects.get(id=_id)

    @staticmethod
    def delete_job_offer_details(job_offer_details: JobOfferDetails):
        job_offer_details.delete()

    @staticmethod
    def delete_job_offer_by_id(_id: int):
        job_offer_details = JobOfferDetailsService.get_job_offer_details_by_id(_id=_id)
        job_offer_details.delete()

    @staticmethod
    def edit_job_offer_by_id(_id: int, motivation_letter, commit=True) -> JobOfferDetails:
        job_offer_details = JobOfferDetailsService.get_job_offer_details_by_id(_id=_id)
        job_offer_details.motivation_letter = motivation_letter

        if commit:
            job_offer_details.save()

        return job_offer_details
