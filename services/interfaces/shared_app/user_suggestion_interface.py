from abc import ABC, abstractmethod

from django.contrib.contenttypes.models import ContentType

from shared_app.models import UserSuggestion


class UserSuggestionInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_user_suggestion(field_name: str,
                               suggestion: str,
                               content_type: ContentType,
                               object_id: int,
                               commit=True) -> UserSuggestion:
        pass

    @staticmethod
    @abstractmethod
    def get_user_suggestion_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_suggestion(user_suggestion: UserSuggestion):
        pass

    @staticmethod
    @abstractmethod
    def delete_suggestion_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_user_suggestion_by_id(_id: int,
                                   field_name: str,
                                   suggestion: str,
                                   content_type: ContentType,
                                   object_id: int,
                                   commit=True) -> UserSuggestion:
        pass
