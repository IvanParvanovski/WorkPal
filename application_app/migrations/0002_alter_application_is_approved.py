# Generated by Django 5.0.1 on 2024-02-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]