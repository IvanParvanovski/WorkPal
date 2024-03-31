from django import template

from services.generic.company_profiles_app.employment_service import EmploymentService

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='is_associate')
def is_associate_in_company(user, company_id):
    associates = [a.profile.user.id for a in EmploymentService.get_associates_for_company(company_id=company_id)]
    return user.id in associates
