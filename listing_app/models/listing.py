from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    location = models.CharField(max_length=250, blank=False, null=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    images = models.FileField()
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
