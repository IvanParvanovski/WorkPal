from django.core.management import BaseCommand

from listing_app.models.industry import Industry


class Command(BaseCommand):
    help = 'Load all industries for deployment'

    def handle(self, *args, **options):
        industries = [
            'Agriculture',
            'Healthcare',
            'Fashion',
            'Technology',
            'Finance',
            'Education',
            'Entertainment',
            'Media',
            'Energy',
            'Food & Beverage',
            'Environmental',
            'Marketing',
            'Sports',
            'Tourism',
            'Retail',
            'Construction',
            'Consulting',
            'Insurance',
            'Biotechnology',
            'Music',
            'Robotics',
            'Artificial Intelligence',
            'Architecture',
            'Real Estate',
            'Interior Design',
            'E-commerce',
            'Aerospace',
        ]

        for industry_name in industries:
            Industry.objects.get_or_create(name=industry_name)
