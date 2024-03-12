from django.contrib.contenttypes.models import ContentType

from accounts_app.models.profile import Profile
from application_app.models import Application
from application_app.models.job_offer_application_details import JobOfferApplicationDetails
from application_app.models.project_application_details import ProjectApplicationDetails
from listing_app.models.listing import Listing
from services.interfaces.application_app.application_interface import ApplicationInterface


class ApplicationService(ApplicationInterface):
    @staticmethod
    def create_application(profile: Profile,
                           listing: Listing,
                           content_type: ContentType,
                           object_id: int,
                           commit=True) -> Application:

        application = Application.objects.create(
            is_approved=False,
            profile=profile,
            listing=listing,
            content_type=content_type,
            object_id=object_id
        )

        if commit:
            application.save()

        return application

    @staticmethod
    def set_application_is_checked_true(application):
        application.is_checked = True
        application.save()
        return application

    @staticmethod
    def set_application_is_approved_true(application):
        application.is_approved = True
        application.save()
        return application

    @staticmethod
    def get_all_applications():
        return Application.objects.all()

    @staticmethod
    def get_application_by_id(_id: int) -> Application:
        return Application.objects.get(id=_id)

    @staticmethod
    def get_applications_by_profile_id(profile_id: int):
        return Application.objects.filter(profile_id=profile_id)

    @staticmethod
    def get_applications_for_user_project(project):
        return Application.objects.filter(listing_id=project.listing.id,
                                          is_checked=False,
                                          content_type_id=ContentType.objects
                                                                     .get_for_model(ProjectApplicationDetails).id)

    @staticmethod
    def get_applications_for_user_projects(projects):
        result = []
        for p in projects:
            result.append(ApplicationService.get_applications_for_user_project(p))

        return result

    @staticmethod
    def get_applications_for_job_offer(job_offer):
        # a functionality to check if the person who is part of the company is applying for the job
        return Application.objects.filter(listing_id=job_offer.listing.id,
                                          is_checked=False)

    @staticmethod
    def get_applications_for_companies_job_offers(companies_job_offers):
        result = []
        for company_job_offers in companies_job_offers:
            for company_job_offer in company_job_offers:
                result.append(ApplicationService.get_applications_for_job_offer(company_job_offer))
        return result

    @staticmethod
    def delete_application(application: Application):
        application.delete()

    @staticmethod
    def delete_application_by_id(_id: int):
        application = ApplicationService.get_application_by_id(_id=_id)
        application.delete()

    @staticmethod
    def edit_application_by_id(_id: int,
                               profile: Profile,
                               listing: Listing,
                               content_type: ContentType,
                               commit=True):

        application = ApplicationService.get_application_by_id(_id=_id)

        application.profile = profile
        application.listing = listing
        application.content_type = content_type

        if commit:
            application.save()

        return application

