from django.db import models

from listing_app.models.industry import Industry


class Listing(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    location = models.CharField(max_length=250, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    images = models.ImageField(upload_to='images/projects/')
    description = models.TextField(blank=False, null=False)
    industries = models.ManyToManyField(Industry)

    def __str__(self):
        return self.title
