# Generated by Django 5.0.1 on 2024-02-28 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0004_remove_listingidentifiers_listing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefits', models.TextField(blank=True, max_length=1500)),
                ('salary_range_min', models.PositiveIntegerField(default=1000)),
                ('salary_range_max', models.PositiveIntegerField(default=5000)),
                ('work_environment', models.CharField(blank=True, choices=[('hybrid', 'Hybrid'), ('remote', 'Remote'), ('in_office', 'In-office'), ('other', 'Other')], max_length=25)),
                ('work_commitment', models.CharField(blank=True, choices=[('full_time', 'Full-Time'), ('part_time', 'Part-Time'), ('zero_hours', 'Zero-Hours'), ('flextime', 'Flextime'), ('other', 'Other')], max_length=50)),
                ('key_responsibilities', models.TextField(blank=True, max_length=1500)),
                ('required_qualifications', models.TextField(blank=True, max_length=1500)),
                ('preferred_qualifications', models.TextField(blank=True, max_length=1500)),
                ('remote_option', models.BooleanField(default=False)),
                ('listing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_offer', to='listing_app.listing')),
            ],
        ),
        migrations.CreateModel(
            name='ListingIdentifiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=96)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='listing_app.listing')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wage', models.PositiveIntegerField()),
                ('preferred_payment', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('in_progress', 'In-progress'), ('open', 'Open'), ('completed', 'Completed')], max_length=20)),
                ('estimated_duration', models.CharField(max_length=50)),
                ('listing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='listing_app.listing')),
            ],
        ),
    ]
