from django.db import models


class JobOfferApplicationDetails(models.Model):
    cv = models.FileField()
    motivation_letter = models.TextField()
