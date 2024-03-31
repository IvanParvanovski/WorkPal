from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'create a group (RightsManager) and assign permissions (give_rights)'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='RightsManager')
        permission_give_rights = Permission.objects.get(codename='give_rights')
        group.permissions.add(permission_give_rights)

        if created:
            self.stdout.write(self.style.SUCCESS('Group "RightsManager" created with permission '
                                                 'give_rights'))
        else:
            self.stdout.write(self.style.WARNING('Group "RightsManager" already exists'))
