from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='ListingsManager')

        permission_create_job_offer = Permission.objects.get(codename='add_joboffer')
        permission_delete_job_offer = Permission.objects.get(codename='delete_joboffer')
        permission_edit_job_offer = Permission.objects.get(codename='change_joboffer')
        permission_edit_company = Permission.objects.get(codename='change_company')
        permission_delete_company = Permission.objects.get(codename='delete_company')

        group.permissions.add(permission_create_job_offer)
        group.permissions.add(permission_delete_job_offer)
        group.permissions.add(permission_edit_job_offer)
        group.permissions.add(permission_edit_company)
        group.permissions.add(permission_delete_company)

        if created:
            self.stdout.write(self.style.SUCCESS('Group "ListingsManager" created with permissions'
                                                 'add_joboffer'
                                                 'delete_joboffer'
                                                 'change_joboffer'))
        else:
            self.stdout.write(self.style.WARNING('Group "ListingsManager" already exists'))
