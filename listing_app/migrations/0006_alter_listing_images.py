# Generated by Django 5.0.1 on 2024-03-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0005_joboffer_listingidentifiers_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='images',
            field=models.FileField(upload_to=''),
        ),
    ]