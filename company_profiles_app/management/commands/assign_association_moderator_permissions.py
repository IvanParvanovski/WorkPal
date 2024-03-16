from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'create a group (AssociatesModerator) and assign permissions (verify_associate)'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='AssociatesModerator')
        permission = Permission.objects.get(codename='verify_associate')
        group.permissions.add(permission)

        if created:
            self.stdout.write(self.style.SUCCESS('Group "Associates Moderator" created with permission '
                                                 '"verify_associates"'))
        else:
            self.stdout.write(self.style.WARNING('Group "Associates Moderator" already exists'))
