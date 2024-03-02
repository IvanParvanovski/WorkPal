from company_profiles_app.models import Company
from company_profiles_app.models.company_identifiers import CompanyIdentifiers
from services.interfaces.company_profiles_app.company_identifiers_interface import CompanyIdentifiersInterface


class CompanyIdentifiersService(CompanyIdentifiersInterface):
    @staticmethod
    def create_company_identifier(_type: str, value, company: Company, commit=True) \
            -> CompanyIdentifiers:

        identifier = CompanyIdentifiers.objects.create(
            type=_type,
            value=value,
            company=company
        )

        if commit:
            identifier.save()

        return identifier

    @staticmethod
    def get_identifier_by_id(_id: int):
        return CompanyIdentifiers.objects.get(id=_id)

    @staticmethod
    def delete_identifier(identifier: CompanyIdentifiers):
        identifier.delete()

    @staticmethod
    def delete_identifier_by_id(_id: int):
        identifier = CompanyIdentifiersService.get_identifier_by_id(_id=_id)
        identifier.delete()

    @staticmethod
    def edit_identifier_by_id(_id: int, _type: str, value, company: Company, commit=True) \
            -> CompanyIdentifiers:

        identifier = CompanyIdentifiersService.get_identifier_by_id(_id=_id)

        identifier.type = _type
        identifier.value = value
        identifier.company = company

        if commit:
            identifier.save()

        return identifier
