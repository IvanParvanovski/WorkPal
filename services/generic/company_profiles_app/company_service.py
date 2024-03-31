from company_profiles_app.models import Company
from services.interfaces.company_profiles_app.company_interface import CompanyInterface


class CompanyService(CompanyInterface):
    @staticmethod
    def create_company(address: str,
                       secondary_address: str,
                       name: str,
                       company_logo,
                       website: str,
                       commit=True):

        company = Company(
            address=address,
            secondary_address=secondary_address,
            company_logo=company_logo,
            name=name,
            website=website
        )

        if commit:
            company.save()

        return company

    @staticmethod
    def get_company_by_id(_id: int):
        return Company.objects.get(id=_id)

    @staticmethod
    def get_user_companies(profile_id: int):
        return Company.objects.filter(employment__is_associate=True,
                                      employment__profile_id=profile_id).distinct()

    @staticmethod
    def delete_company_by_id(_id: int):
        company = CompanyService.get_company_by_id(_id)
        company.delete()

    @staticmethod
    def get_verified_companies(search_text):
        return Company.objects.filter(name__icontains=search_text,
                                      is_verified=True)

    @staticmethod
    def delete_company(company: Company):
        company.delete()

    @staticmethod
    def edit_company(_id: int,
                     address: str,
                     secondary_address: str,
                     name: str,
                     company_logo,
                     website: str,
                     commit=True):

        company = CompanyService.get_company_by_id(_id)

        company.address = address
        company.secondary_address = secondary_address
        company.company_logo = company_logo
        company.name = name
        company.website = website

        if commit:
            company.save()

        return company
