# Generated by Django 5.0.1 on 2024-02-18 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobOfferProxy',
            new_name='JobOffer',
        ),
        migrations.RenameModel(
            old_name='ProjectProxy',
            new_name='Project',
        ),
    ]
