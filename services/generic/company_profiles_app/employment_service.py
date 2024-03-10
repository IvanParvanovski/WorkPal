from accounts_app.models.profile import Profile
from company_profiles_app.models import Employment, Company
from services.interfaces.company_profiles_app.employment_interface import EmploymentInterface


class EmploymentService(EmploymentInterface):
    @staticmethod
    def create_employment(profile: Profile, company: Company, job_title: str, commit=True)\
            -> Employment:

        employment = Employment(
            profile=profile,
            company=company,
            job_title=job_title,
            is_associate=False
        )

        if commit:
            employment.save()

        return employment

    @staticmethod
    def get_all_employments():
        return Employment.objects.all()

    @staticmethod
    def get_employment_by_id(_id: int):
        return Employment.objects.get(id=_id)

    @staticmethod
    def get_association_requests_by_company_id(_id: int):
        return Employment.objects.filter(company_id=_id,
                                         is_associate=False)


    @staticmethod
    def delete_employment(employment):
        employment.delete()

    @staticmethod
    def delete_employment_by_id(_id: int):
        employment = EmploymentService.get_employment_by_id(_id=_id)
        employment.delete()

    @staticmethod
    def set_employment_is_associate_to_true(employment: Employment):
        employment.is_associate = True
        return employment

    @staticmethod
    def edit_employment_by_id(
            _id: int,
            profile: Profile,
            company: Company,
            job_title: str,
            commit=True) -> Employment:

        employment = EmploymentService.get_employment_by_id(_id=_id)

        employment.profile = profile
        employment.company = company
        employment.job_title = job_title

        if commit:
            employment.save()

        return employment

