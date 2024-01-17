# Generated by Django 5.0.1 on 2024-01-14 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0005_rename_company_id_companyemails_company_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': [('verify_company', 'Can verify the company if it is legit')]},
        ),
        migrations.AddField(
            model_name='company',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(choices=[('owner', 'Owner'), ('human_resources', 'Human Resources'), ('recruiter', 'Recruiter'), ('hiring_manager', 'Hiring Manager'), ('employee', 'Employee'), ('intern', 'Intern'), ('other', 'Other')], max_length=15)),
                ('is_associate', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_app.company')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_app.profile')),
            ],
            options={
                'permissions': [('verify_associate', 'Can verify if a person is associated with the given company')],
            },
        ),
    ]