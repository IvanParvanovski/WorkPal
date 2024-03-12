from listing_app.models.industry import Industry
from services.interfaces.listing_app.industry_interface import IndustryInterface


class IndustryService(IndustryInterface):
    @staticmethod
    def create_industry(name, commit=True):
        industry = Industry.objects.create(name=name)

        if commit:
            industry.save()

        return industry

    @staticmethod
    def get_all_industries():
        return Industry.objects.all()

    @staticmethod
    def get_industry_by_id(_id: int):
        return Industry.objects.get(id=_id)

    @staticmethod
    def delete_industry_by_id(_id: int):
        industry = IndustryService.get_industry_by_id(_id=_id)
        industry.delete()

    @staticmethod
    def edit_industry_by_id(_id: int,
                            name,
                            commit=True):

        industry = IndustryService.get_industry_by_id(_id)
        industry.name = name

        if commit:
            industry.save()

        return industry
