# Generated by Django 5.0.1 on 2024-03-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profiles_app', '0007_rename_person_employment_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
