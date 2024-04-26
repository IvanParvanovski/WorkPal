from django.contrib.contenttypes.models import ContentType

from services.interfaces.shared_app.user_suggestion_interface import UserSuggestionInterface
from shared_app.models import UserSuggestion


class UserSuggestionService(UserSuggestionInterface):
    @staticmethod
    def create_user_suggestion(field_name: str,
                               suggestion: str,
                               content_type: ContentType,
                               object_id: int,
                               commit=True) -> UserSuggestion:

        user_suggestion = UserSuggestion(
            field_name=field_name,
            suggestion=suggestion,
            content_type=content_type,
            object_id=object_id
        )

        if commit:
            user_suggestion.save()

        return user_suggestion

    @staticmethod
    def get_user_suggestion_by_id(_id: int):
        return UserSuggestion.objects.get(id=_id)

    @staticmethod
    def delete_suggestion(user_suggestion: UserSuggestion):
        user_suggestion.delete()

    @staticmethod
    def delete_suggestion_by_id(_id: int):
        user_suggestion = UserSuggestionService.get_user_suggestion_by_id(_id=_id)
        user_suggestion.delete()

    @staticmethod
    def edit_user_suggestion_by_id(_id: int,
                                   field_name: str,
                                   suggestion: str,
                                   content_type: ContentType,
                                   object_id: int,
                                   commit=True) -> UserSuggestion:
        user_suggestion = UserSuggestionService.get_user_suggestion_by_id(_id=_id)

        user_suggestion.field_name = field_name
        user_suggestion.suggestion = suggestion
        user_suggestion.content_type = content_type
        user_suggestion.object_id = object_id

        if commit:
            user_suggestion.save()

        return user_suggestion
