from django.contrib.contenttypes.models import ContentType

from accounts_app.models.profile import Profile
from application_app.models import Application
from listing_app.models.listing import Listing
from services.interfaces.application_app.application_interface import ApplicationInterface


class ApplicationService(ApplicationInterface):
    @staticmethod
    def create_application(profile: Profile,
                           listing: Listing,
                           content_type: ContentType,
                           object_id: int) -> Application:

        application = Application.objects.create(
            is_approved=False,
            profile=profile,
            listing=listing,
            content_type=content_type,
            object_id=object_id
        )

        application.save()
        return application

    @staticmethod
    def get_all_applications():
        return Application.objects.all()

    @staticmethod
    def get_application_by_id(_id: int) -> Application:
        return Application.objects.get(id=_id)

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
                               content_type: ContentType):

        application = ApplicationService.get_application_by_id(_id=_id)

        application.profile = profile
        application.listing = listing
        application.content_type = content_type

        application.save()
        return application
