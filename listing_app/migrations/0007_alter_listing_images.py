# Generated by Django 5.0.1 on 2024-03-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0006_alter_listing_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='images',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]
