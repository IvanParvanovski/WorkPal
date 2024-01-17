# Generated by Django 5.0.1 on 2024-01-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication_app', '0006_alter_company_options_company_is_deleted_employment'),
    ]

    state_operations = [
        migrations.AlterField(
            model_name='profile',
            name='companies',
            field=models.ManyToManyField(through='authentication_app.Employment', to='authentication_app.company'),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),
        migrations.AlterModelTable(
            name='employment',
            table=None,
        ),
    ]
