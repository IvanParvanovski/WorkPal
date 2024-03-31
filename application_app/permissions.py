from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect

from services.generic.accounts_app.profile_service import ProfileService


@permission_required('company_profiles_app.give_rights', raise_exception=True)
def make_application_moderator(reqeust, *args, **kwargs):
    profile_id = kwargs.get('user_to_grant_rights_id')

    user_to_grant_rights = ProfileService.get_profile_by_id(profile_id).user
    application_moderator_group = Group.objects.get(name='ApplicationModerator')
    user_to_grant_rights.groups.add(application_moderator_group)

    return redirect('user_associates')
