from abc import ABC, abstractmethod

from accounts_app.models import CustomUser


class CustomUserInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_custom_user(first_name: str,
                           last_name: str,
                           username: str,
                           email: str,
                           password: str,
                           commit=True) -> CustomUser:
        pass

    @staticmethod
    @abstractmethod
    def get_user_by_id(_id: int) -> CustomUser:
        pass

    @staticmethod
    @abstractmethod
    def delete_user(user: CustomUser):
        pass

    @staticmethod
    @abstractmethod
    def delete_user_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_user_by_id(_id: int,
                        first_name: str,
                        last_name: str,
                        username: str,
                        email: str,
                        password: str,
                        commit=True) -> CustomUser:
        pass
