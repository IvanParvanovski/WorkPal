from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


# def has_company_permission(user, model, app_name, permission, company_name):
#     """
#     :param user: User
#     :param app_name: company_profiles_app
#     :param permission: add_job_offer
#     :param company_name: BMW
#     :return: company_profiles_app.add_job_offer_bmw
#     """
#
#     permission_codename = f'{permission}_{company_name.lower().replace(" ", "_")}'
#     print(app_name)
#
#     content_type = ContentType.objects.get(app_label=app_name, model=model)
#
#     permission = Permission.objects.get(content_type=content_type, codename=permission_codename)
#
#     return user.has_perm(permission)


def has_company_permission(user, app_name, permission, company_name):
    return user.has_perm(f'{app_name}.{permission}_{company_name.lower().replace(" ", "_")}')
