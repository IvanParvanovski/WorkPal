from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect

from services.generic.accounts_app.profile_service import ProfileService


@permission_required('company_profiles_app.give_rights', raise_exception=True)
def make_associate_moderator(request, *args, **kwargs):
    profile_id = kwargs.get('profile_id')

    request_initiator = ProfileService.get_profile_by_id(profile_id).user
    associates_moderator_group = Group.objects.get(name='AssociatesModerator')
    request_initiator.groups.add(associates_moderator_group)

    return redirect('user_associates')
