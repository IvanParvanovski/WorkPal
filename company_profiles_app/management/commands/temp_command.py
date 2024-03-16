from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from services.generic.accounts_app.custom_user_service import CustomUserService


class Command(BaseCommand):
    help = 'create a group and assign permissions'

    def handle(self, *args, **options):
        user = CustomUserService.get_user_by_id(_id=8)
        associates_moderator_group = Group.objects.get(name='AssociatesModerator')
        user.groups.add(associates_moderator_group)
