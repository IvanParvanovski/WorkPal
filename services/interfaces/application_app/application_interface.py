from abc import ABC, abstractmethod

from django.contrib.contenttypes.models import ContentType

from accounts_app.models.profile import Profile
from application_app.models import Application
from listing_app.models.listing import Listing


class ApplicationInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_application(profile: Profile,
                           listing: Listing,
                           content_type: ContentType,
                           object_id: int,
                           commit=True) -> Application:
        pass

    @staticmethod
    @abstractmethod
    def get_all_applications():
        pass

    @staticmethod
    @abstractmethod
    def get_application_by_id(_id: int) -> Application:
        pass

    @staticmethod
    @abstractmethod
    def get_applications_by_profile_id(profile_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_application(application: Application):
        pass

    @staticmethod
    @abstractmethod
    def edit_application_by_id(_id: int,
                               profile: Profile,
                               listing: Listing,
                               content_type: ContentType,
                               commit=True):
        pass
