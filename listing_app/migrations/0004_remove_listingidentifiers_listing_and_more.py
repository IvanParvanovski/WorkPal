# Generated by Django 5.0.1 on 2024-02-28 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0003_alter_joboffer_listing_alter_project_listing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingidentifiers',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='project',
            name='listing',
        ),
        migrations.DeleteModel(
            name='JobOffer',
        ),
        migrations.DeleteModel(
            name='ListingIdentifiers',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
