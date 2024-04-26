from company_profiles_app.models import Company
from company_profiles_app.models.company_identifiers import CompanyIdentifiers
from services.interfaces.company_profiles_app.company_identifiers_interface import CompanyIdentifiersInterface


class CompanyIdentifiersService(CompanyIdentifiersInterface):
    @staticmethod
    def create_company_identifier(_type: str, value, company: Company, commit=True) \
            -> CompanyIdentifiers:

        identifier = CompanyIdentifiers(
            type=_type,
            value=value,
            company=company
        )

        if commit:
            identifier.save()

        return identifier

    @staticmethod
    def create_company_identifier_email(value, company: Company, commit=True) \
            -> CompanyIdentifiers:
        return CompanyIdentifiersService.create_company_identifier(_type='email',
                                                                   value=value,
                                                                   company=company,
                                                                   commit=commit)

    @staticmethod
    def create_company_identifier_phone_number(value, company: Company, commit=True) \
            -> CompanyIdentifiers:
        return CompanyIdentifiersService.create_company_identifier(_type='phone_number',
                                                                   value=value,
                                                                   company=company,
                                                                   commit=commit)

    @staticmethod
    def get_company_identifier_phone_number(company_id):
        return CompanyIdentifiers.objects.filter(company_id=company_id,
                                                 type='phone_number')[0]

    @staticmethod
    def get_company_identifier_email(company_id):
        return CompanyIdentifiers.objects.filter(company_id=company_id,
                                                 type='email')[0]

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
