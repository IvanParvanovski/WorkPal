# models in this folder will not be migrated because the app
# is not installed in the settings apps
from django.db import models


class UserSuggestionAbstract(models.Model):
    """
    The child class should inherit the superclass and models.Model
    """
    field_name = models.CharField(max_length=100)
    suggestion = models.CharField(max_length=100)

    class Meta:
        abstract = True

