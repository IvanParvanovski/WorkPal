from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='CompanyManager')
        permission_delete = Permission.objects.get(codename='delete_company')
        permission_edit = Permission.objects.get(codename='change_company')

        group.permissions.add(permission_delete)
        group.permissions.add(permission_edit)

        if created:
            self.stdout.write(self.style.SUCCESS('Group "CompanyManager" created with permissions '
                                                 'delete_company, change_company'))
        else:
            self.stdout.write(self.style.SUCCESS('Group "CompanyManager" already exists'))
