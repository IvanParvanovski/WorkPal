from accounts_app.models import CustomUser
from services.interfaces.accounts_app.custom_user_interface import CustomUserInterface


class CustomUserService(CustomUserInterface):
    @staticmethod
    def create_custom_user(username: str, email: str, password: str) -> CustomUser:
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        return user

    @staticmethod
    def get_user_by_id(_id: int) -> CustomUser:
        return CustomUser.objects.get(id=_id)

    @staticmethod
    def delete_user(user: CustomUser):
        user.delete()

    @staticmethod
    def delete_user_by_id(_id: int):
        user = CustomUserService.get_user_by_id(_id=_id)
        user.delete()

    @staticmethod
    def edit_user_by_id(_id: int, username: str, email: str, password: str) -> CustomUser:
        user = CustomUserService.get_user_by_id(_id=_id)

        user.username = username
        user.email = email
        user.password = password

        user.save()

        return user
