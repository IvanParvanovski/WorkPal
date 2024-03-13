from abc import ABC, abstractmethod


class IndustryInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_industry(name, commit=True):
        pass

    @staticmethod
    @abstractmethod
    def get_all_industries():
        pass

    @staticmethod
    @abstractmethod
    def get_industry_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def get_industry_by_name(name):
        pass

    @staticmethod
    @abstractmethod
    def delete_industry_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_industry_by_id(_id: int,
                            name,
                            commit=True):
        pass
