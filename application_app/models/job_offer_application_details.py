from django.db import models


class JobOfferApplicationDetails(models.Model):
    cv = models.FileField(upload_to='files/')
    motivation_letter = models.TextField()
