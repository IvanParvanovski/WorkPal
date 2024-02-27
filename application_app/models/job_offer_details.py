from django.db import models


class JobOfferDetails(models.Model):
    cv = models.FileField()
    motivation_letter = models.TextField()
