# Generated by Django 5.0.1 on 2024-03-06 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_profiles_app', '0006_companyidentifiers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employment',
            old_name='person',
            new_name='profile',
        ),
    ]
