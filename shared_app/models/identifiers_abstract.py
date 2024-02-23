from django.db import models


class IdentifiersAbstract(models.Model):
    """
    Provides an interface for contacts. The type can be any sort of social media or address.
    For example, type can be 'email' and value can be 'example@example.com'
    """
    type = models.CharField(max_length=40)
    value = models.CharField(max_length=96)

    class Meta:
        abstract = True
