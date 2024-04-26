from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from services.generic.accounts_app.profile_service import ProfileService
from services.generic.company_profiles_app.company_service import CompanyService
from shared_app.utils import has_company_permission


def make_associate_moderator(request, *args, **kwargs):
    profile_id = kwargs.get('user_to_grant_rights_id')
    company_id = kwargs.get('company_id')
    company = CompanyService.get_company_by_id(company_id)

    if not has_company_permission(request.user,
                                  'company_profiles_app',
                                  'can_give_rights',
                                  company.name):
        raise PermissionDenied

    user_to_grant_rights = ProfileService.get_profile_by_id(profile_id).user
    instance_name = company.name.lower().replace(" ", "_")

    permission_verify_associate = Permission.objects.get(codename=f'can_verify_associate_{instance_name}')


    user_to_grant_rights.user_permissions.add(permission_verify_associate)

    return redirect('user_associates')
