from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='ApplicationModerator')

        permission_accept_or_reject_application = Permission.objects.get(codename='adjudicate_application')

        group.permissions.add(permission_accept_or_reject_application)
        group.permissions.add()

        if created:
            self.stdout.write(self.style.SUCCESS('Group ApplicationModerator created '))
        else:
            self.stdout.write(self.style.WARNING('Group ApplicationModerator already exists'))
