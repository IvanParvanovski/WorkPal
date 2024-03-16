from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect

from services.generic.accounts_app.profile_service import ProfileService


@permission_required('company_profiles_app.give_rights', raise_exception=True)
def make_rights_manager(request, *args, **kwargs):
    profile_id = kwargs.get('user_to_grant_rights_id')

    user_to_grant_rights = ProfileService.get_profile_by_id(profile_id).user
    rights_manager_group = Group.objects.get(name='RightsManager')
    user_to_grant_rights.groups.add(rights_manager_group)

    return redirect('user_associates')
