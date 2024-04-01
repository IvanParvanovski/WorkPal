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


@register.filter(name='format_value')
def format_value(value):
    # Split the value by underscores and capitalize each word
    formatted_value = ' '.join(word.capitalize() for word in value.split('_'))
    return formatted_value


@register.filter(name='format_salary')
def format_salary(value):
    if value < 1000:
        return '${:,.0f}'.format(value)  # Format smaller salaries without K or M
    elif value < 1000000:
        return '${:,.0f}K'.format(value / 1000)  # Convert to K
    else:
        return '${:,.1f}M'.format(value / 1000000)


@register.filter(name='calculate_days_since_creation')
def calculate_days_since_creation(date_updated, date_created):
    difference = date_updated - date_created

    return difference.days
